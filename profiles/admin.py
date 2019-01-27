from django.contrib import admin
from profiles.models import PictureModel, SkillModel, ProfileModel, PortfolioModel, LinkModel, LevelModel, EducationModel, CertificationModel, MajorModel, SchoolModel
# Register your models here.

class SkillModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class LevelModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'skill', 'skill_level']

class LinkModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'user']

class CertificationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

class EducationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'major', 'school', 'status', 'degree_type']

class MajorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class SchoolModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(SkillModel, SkillModelAdmin)
admin.site.register(ProfileModel)
admin.site.register(PortfolioModel)
admin.site.register(LinkModel, LinkModelAdmin)
admin.site.register(LevelModel, LevelModelAdmin)
admin.site.register(EducationModel, EducationModelAdmin)
admin.site.register(CertificationModel, CertificationModelAdmin)
admin.site.register(MajorModel, MajorModelAdmin)
admin.site.register(SchoolModel, SchoolModelAdmin)

