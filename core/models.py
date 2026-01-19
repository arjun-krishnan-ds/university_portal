from django.db import models
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.html import format_html


class Programs(models.Model):
    LEVEL_CHOICES = [
        ("UG", "Undergraduate"),
        ("PG", "Postgraduate"),
        ("PHD", "Doctoral"),
    ]

    p_name = models.CharField(max_length=100)
    p_desc = models.TextField()
    p_dur = models.CharField(
        max_length=20
    )  # Could be months/years, keep as CharField for now
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.p_name} ({self.level})"


class Departments(models.Model):
    d_name = models.CharField(max_length=300)
    d_desc = models.TextField()
    d_num = models.PositiveIntegerField(default=0, editable=False)  # Number of faculty

    def __str__(self):
        return self.d_name
# ===================== Departments Model =====================
class Departments(models.Model):
    d_name = models.CharField(max_length=300)
    d_desc = models.TextField()
    d_num = models.PositiveIntegerField(default=0, editable=False)  # Number of faculty

    def __str__(self):
        return self.d_name

# ===================== Faculty Model =====================
class Faculty(models.Model):
    f_name = models.CharField("Faculty Name", max_length=200)
    f_img = models.ImageField("Profile Image", upload_to="faculty/", blank=True, null=True)
    f_sub = models.ManyToManyField("Subjects", blank=True, verbose_name="Subjects")
    f_dep = models.ForeignKey(
        Departments, 
        on_delete=models.CASCADE, 
        related_name="faculties",
        verbose_name="Department"
    )

    def __str__(self):
        return self.f_name

    # Optional: thumbnail for admin display
    def image_tag(self):
        if self.f_img:
            return format_html('<img src="{}" style="height:50px;width:50px;"/>', self.f_img.url)
        return ""
    image_tag.short_description = 'Photo'

# ===================== Signals to update d_num =====================
@receiver([post_save, post_delete], sender=Faculty)
def update_department_faculty_count(sender, instance, **kwargs):
    """
    Updates the d_num field of Departments whenever a Faculty is added or removed.
    """
    department = instance.f_dep
    department.d_num = department.faculties.count()
    department.save(update_fields=['d_num'])

class Subjects(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Admission(models.Model):
    adm_win_name = models.CharField(max_length=200)
    adm_win_sts = models.CharField(
        max_length=20, choices=[("Open", "Open"), ("Closed", "Closed")], default="Open"
    )
    adm_win_start = models.DateField()
    adm_win_close = models.DateField()
    adm_elg = models.TextField()

    def __str__(self):
        return f"{self.adm_win_name} ({self.adm_win_sts})"


def validate_pdf(file):
    max_size = 5 * 1024 * 1024  # 5MB limit
    if file.size > max_size:
        raise ValidationError(f"File too large! Maximum size allowed is 5MB.")


class AdmissionApplication(models.Model):
    QUALIFICATION_CHOICES = [
        ("high_school", "High School"),
        ("graduate", "Graduate"),
        ("post_graduate", "Post Graduate"),
    ]

    applicant_name = models.CharField(max_length=200)
    program = models.ForeignKey(
        Programs, on_delete=models.CASCADE, related_name="applications"
    )
    email = models.EmailField(unique=True)
    previous_qualification = models.CharField(
        max_length=50, choices=QUALIFICATION_CHOICES
    )
    certificates = models.FileField(upload_to="certificates/")
    nationality = CountryField(blank_label="Select nationality")
    phone_country_code = models.CharField(max_length=10)
    local_phone_number = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.applicant_name
