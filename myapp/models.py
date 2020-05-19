from django.db import models

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=30)
    esname=models.CharField(max_length=40)
    mobno=models.IntegerField()
    email=models.EmailField()
