from django.db import models
from django.contrib import admin

class movie(models.Model):
    mid = models.CharField(max_length=20, help_text="Employee ID")
    name = models.CharField(max_length=100)
    cost = models.IntegerField(max_length=100)
    mtype = models.CharField(max_length=100)
    mlength = models.FloatField()

class movieAdmin(admin.ModelAdmin):
    list_display = ('mid', 'name', 'cost', 'mtype', 'mlength')
