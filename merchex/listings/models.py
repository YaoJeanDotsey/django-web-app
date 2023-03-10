from django.db import models
from django.contrib import admin

# Create your models here.

class Band(models.Model):

    class Type(models.TextChoices):
        records = "REC"
        clothing = "CLOTH"
        posters = "POST"
        miscellaneous = "MISCELLA"

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null = True, blank = True)
    type = models.CharField( max_length=10)

class BandAdmin(admin.ModelAdmin): 
    list_display = ('name', 'sold', 'year') 