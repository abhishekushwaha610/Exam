from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE,to=User)
    college = models.CharField(max_length=100)
    sem = models.CharField(max_length=1)
    branch = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=2)

    def __str__(self):
        return str(self.user)
