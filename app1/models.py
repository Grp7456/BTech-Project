from inspect import stack
from django.db import models

class Usertable(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    pswrd=models.CharField(max_length=200)
