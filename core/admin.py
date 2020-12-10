from django.contrib import admin

from .models import Education, Skill, ExtraEducation, Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'city', 'state', 'phone', 'email', 'facebook', 'twitter', 'youtube', 'linkedin', 'instagram', "github")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'start', 'end', 'city', 'state')


@admin.register(ExtraEducation)
class ExtraEducationAdmin(admin.ModelAdmin):
    list_display = ('name',)


