from django.contrib import admin
from profiles.models import PictureModel, SkillModel, ProfileModel, PortfolioModel, LinkModel, LevelModel
# Register your models here.

class SkillModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class LevelModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'skill', 'skill_level']

class LinkModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'user']

admin.site.register(PictureModel)
admin.site.register(SkillModel, SkillModelAdmin)
admin.site.register(ProfileModel)
admin.site.register(PortfolioModel)
admin.site.register(LinkModel, LinkModelAdmin)
admin.site.register(LevelModel, LevelModelAdmin)