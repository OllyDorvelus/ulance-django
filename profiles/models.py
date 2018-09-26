from django.db import models
from django.conf import settings
import uuid
# Create your models here.

class PortfolioModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PictureModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to='pictures')
    description = models.TextField(max_length=250, blank=True, null=True)
    portfolio = models.ForeignKey(PortfolioModel, related_name='pictures', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

class SkillModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    # BEGINNER = 'BG'
    # INTERMEDIATE = 'IT'
    # EXPERT = 'EX'
    # SKILL_LEVEL_CHOICES = (
    #     (BEGINNER, 'Beginner'),
    #     (INTERMEDIATE, 'Intermediate'),
    #     (EXPERT, 'Expert'),
    # )
    # skill_level = models.CharField(max_length=2, choices=SKILL_LEVEL_CHOICES, default=BEGINNER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LevelModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
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
        return self.skill.name + '-' + self.skill_level + '-' + self.user.username

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

class LinkModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField(blank=False, null=False, max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='links', on_delete=models.CASCADE, null=False)
    brief_description = models.CharField(max_length=75, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







