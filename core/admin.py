from django.contrib import admin
from .models import Programs, Departments, Faculty, Admission, AdmissionApplication,Subject

# Register your models here.
admin.site.register(Programs)
admin.site.register(Departments)
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("f_name", "f_dep", "subjects_list")
    filter_horizontal = ("f_sub",)

admin.site.register(Admission)
@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'program', 'email', 'previous_qualification', 'submitted_at')
    readonly_fields = ('submitted_at',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

