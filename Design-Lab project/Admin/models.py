from django.db import models

# Create your models here.

class ArchDesRegisterDB(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(default=0)
    image = models.ImageField(upload_to='Register_Architect', null=True, blank=True)