from django.contrib import admin
from .models import Programs,Departments,Faculty,Admission

# Register your models here.
admin.site.register(Programs)
admin.site.register(Departments)
admin.site.register(Faculty)
admin.site.register(Admission)