from django.db import models

# Create your models here.


class addPlansDB(models.Model):
    plan = models.CharField(max_length=100, null=True, blank=True)
    squarefeet = models.IntegerField(null=True, blank=True)
    numberbedrooms = models.IntegerField(null=True, blank=True)
    numberbathrooms = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='add_plans')
    architect = models.CharField(max_length=100, null=True, blank=True)


class addDesignsDB(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    style = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    material = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='add_designs')
    designer = models.CharField(max_length=100, null=True, blank=True)
    