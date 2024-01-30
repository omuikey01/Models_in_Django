from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    password = models.CharField(max_length=50)
    co_pass = models.CharField(max_length=50)
