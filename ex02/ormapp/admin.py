from django.contrib import admin
from .models import movie, movieAdmin

admin.site.register(movie, movieAdmin)
