from django.db import models
from account.models import Teacher,Student
from tinymce.models import HTMLField
from uuid import uuid4
class Exam(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    sem = models.CharField(max_length=1)
    start_date = models.DateField(auto_now=True) # abhi k liye ese hi
    start_time = models.TimeField(auto_now=True) # is bhi 
    end_time = models.TimeField(auto_now=True) # abhi k liye ese hi
    unique = models.UUIDField(default=uuid4().hex,unique=True)
    def __str__(self):
        return self.name

class Question(models.Model):

    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    question = HTMLField()
    # answer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question

class Options(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    option = models.CharField(max_length=20)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.option

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    score = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.student)
