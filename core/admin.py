from django.contrib import admin
from .models import Programs, Departments, Faculty, Admission, AdmissionApplication

# Register your models here.
admin.site.register(Programs)
admin.site.register(Departments)
admin.site.register(Faculty)
admin.site.register(Admission)
@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'program', 'email', 'previous_qualification', 'submitted_at')
    readonly_fields = ('submitted_at',)
