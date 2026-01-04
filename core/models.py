from django.db import models

# Create your models here.

class Application(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    program = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
class Programs(models.Model):
    LEVEL_CHOICES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('PHD', 'Doctoral'),
    ]
    p_name = models.CharField(max_length=100)
    p_desc = models.CharField(max_length=200)
    p_dur = models.CharField(max_length=20)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    def __str__(self):
        return self.p_name

class Departments(models.Model):
    d_name=models.CharField(max_length=300)
    d_desc=models.CharField(max_length=1000)
    d_num=models.IntegerField()
    def __str__(self):
        return self.d_name
    
class Faculty(models.Model):
    f_name = models.CharField(max_length=200)
    f_img = models.ImageField(upload_to='faculty/', blank=True, null=True)
    f_sub = models.CharField(max_length=100, blank=True, null=True)
    f_dep = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='faculties')

    def __str__(self):
        return self.f_name

class Admission(models.Model):
    adm_win_name= models.CharField(max_length=200)
    adm_win_sts= models.CharField(max_length=200)
    adm_win_start=models.CharField(max_length=100)
    adm_win_close=models.CharField(max_length=100,)
    adm_elg=models.CharField(max_length=200)
    nxt_adm_win_name=models.CharField(max_length=200)
    def __str__(self):
        return self.adm_win_name
