
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class student_id(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    stu_id = models.CharField(max_length=100)
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField(max_length=100)
    stu_con = models.IntegerField()
    stu_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.stu_name


class subjects (models.Model):
    sub = models.CharField (max_length=100)
    rooms =  models.CharField(max_length=100)
    teacher = models.CharField (max_length=100)
    days = models.CharField (max_length=100)
    time = models.IntegerField ()

    def __str__(self):
        return f"{self.sub}"
    

class grade (models.Model):
    stud_id =  models.CharField (max_length=100)
    sub_id =  models.CharField (max_length=100)
    prelims = models.IntegerField ()
    midterms = models.IntegerField ()
    finals = models.IntegerField ()

    def __str__(self):
        return f"{self.stud_id}"
    

class section (models.Model):
    sec_name =  models.CharField (max_length=100)
    course=  models.CharField (max_length=100)
    year_lvl =  models.CharField (max_length=100)
    adviser =  models.CharField (max_length=100)
    homeroom =  models.CharField (max_length=100)
    def __str__(self):
        return f"{self.sec_name}"
    

class teacher_profile(models.Model):
    instructor_id =  models.CharField (max_length=100)
    prof_name = models.CharField(max_length=100)
    instructor_email = models.EmailField (max_length=100)
    contach = models.IntegerField()
    specialized = models.CharField (max_length=100)


    def __str__(self):
        return f"{self.prof_name}"
    



# Create your models here.
