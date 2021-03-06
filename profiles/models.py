import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse, reverse_lazy
from ulance.models import PictureModel
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from . import validators
from decimal import DecimalException
# Create your models here.


# class PortfolioModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
#     description = models.TextField(max_length=500, blank=False, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class SkillModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_parent = models.BooleanField(verbose_name='is a parent category', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.parent:
            return f'{self.parent.name} - {self.name}'
        else:
            return self.name


# class LevelModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE, related_name='skills')
#     skill = models.ForeignKey(SkillModel, blank=False, null=False, on_delete=models.CASCADE)
#     BEGINNER = 'BG'
#     INTERMEDIATE = 'IT'
#     EXPERT = 'EX'
#     SKILL_LEVEL_CHOICES = (
#         (BEGINNER, 'Beginner'),
#         (INTERMEDIATE, 'Intermediate'),
#         (EXPERT, 'Expert'),
#     )
#     skill_level = models.CharField(max_length=2, choices=SKILL_LEVEL_CHOICES, default=BEGINNER)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.skill.name} - {self.skill_level} - {self.user.username}'


class ProfileModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='tc.png', upload_to='profile_pics')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=10000, blank=True, null=True)
    skills = models.ManyToManyField(SkillModel, blank=True, related_name='profile')
    services_completed = models.PositiveIntegerField(blank=True, null=False, default=0)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    average_rating = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profiles:profile-detail', kwargs={'username': self.user.username})

    def get_avg_rating(self):
        if self.user.reviews.count():
            total = 0
            count = 0
            for review in self.user.reviews.all():
                total += review.rate
                count += 1
            avg = total / count
            return round(avg, 2)
        return 0.00

    # def get_services_completed(self):
    #     user = self.user
    #     services = user.services.all()
    #     services_completed = 0
    #     for service in services:
    #         services_completed += EntryModel.objects.filter(service=service, is_ordered=True, status='COM').count()
    #     return services_completed


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


class ReviewModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewer')
    description = models.TextField(blank=False, null=False, max_length=300)
    rate = models.IntegerField(validators=[validators.validate_rate])
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.rate}'

    def clean(self, *args, **kwargs):
        if self.freelancer.profile.reviews.filter(user=self.user):
            raise ValidationError("You already wrote an review")


@receiver(post_save, sender=ReviewModel)
def update_avg_rating_add_or_update(sender, instance, **kwargs):
    if instance.freelancer:
        try:
            freelancer = instance.freelancer
            profile = freelancer.profile
            profile.average_rating = profile.get_avg_rating()
            profile.save()
        except (ValueError, DecimalException):
            pass


@receiver(post_delete, sender=ReviewModel)
def update_avg_rating_delete(sender, instance, **kwargs):
    freelancer = instance.freelancer
    profile = freelancer.profile
    profile.average_rating = profile.get_avg_rating()
    profile.save()









