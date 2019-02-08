from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from ulance.models import PictureModel
from orders.models import EntryModel
import uuid
# Create your models here.


class PortfolioModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SkillModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class LevelModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(SkillModel, blank=False, null=False, on_delete=models.CASCADE)
    BEGINNER = 'BG'
    INTERMEDIATE = 'IT'
    EXPERT = 'EX'
    SKILL_LEVEL_CHOICES = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (EXPERT, 'Expert'),
    )
    skill_level = models.CharField(max_length=2, choices=SKILL_LEVEL_CHOICES, default=BEGINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.skill.name} - {self.skill_level} - {self.user.username}'


class ProfileModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='tc.png', upload_to='profile_pics')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null = True)
    skills = models.ManyToManyField(SkillModel, max_length=50, blank=True)
    services_completed = models.PositiveIntegerField(blank=True, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles:profile-detail', kwargs={'username': self.user.username})

    def get_services_completed(self):
        user = self.user
        services = user.services.all()
        services_completed = 0
        for service in services:
            services_completed += EntryModel.objects.filter(service=service, is_ordered=True, status='COM').count()
        return services_completed


class LinkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(blank=False, null=False, max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links', on_delete=models.CASCADE, null=False)
    brief_description = models.CharField(max_length=75, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link


class MajorModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SchoolModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EducationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='educations', on_delete=models.CASCADE, null=False)
    major = models.ForeignKey(MajorModel, on_delete=models.SET_NULL, null=True, blank=False, related_name='major_name')
    school = models.ForeignKey(SchoolModel, on_delete=models.SET_NULL, null=True, blank=False, related_name='school_name')
    FRESHMAN = 'FR'
    SOPHMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHMORE, 'Sophmore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate')
    )
    DEGREE_TYPE_CHOICES = (
        ('AS', 'A.S.'),
        ('BS', 'B.S.'),
        ('MA', 'M.A.')
    )
    STATUS_CHOICES = (
        ('ONG', 'Ongoing'),
        ('INC', 'Incomplete'),
        ('COM', 'Complete'),
    )
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, blank=False, null=False)
    degree_type = models.CharField(max_length=5, choices=DEGREE_TYPE_CHOICES, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.school.name} - {self.major.name}'


class CertificationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='certifications', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    issued_from = models.CharField(max_length=200, blank=False, null=False)
    year_issued = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name










