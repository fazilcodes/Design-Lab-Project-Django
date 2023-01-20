from django.db import models

# Create your models here.

class customerRegisterDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm = models.CharField(max_length=100, null=True, blank=True)
    