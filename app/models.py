from django.db import models

class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=30,unique=True)
    trainer=models.CharField(max_length=30,null=False)
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)
    

