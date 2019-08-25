from django.db import models

# Create your models here.
class Grade(models.Model):
    g_name = models.CharField(max_length=32)

class Student(models.Model):
    s_grage= models.ForeignKey(Grade)
    s_name = models.CharField(max_length=20)