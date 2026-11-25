from django.contrib import admin
from .models import Certification, Article, Achievement, Interest

admin.site.register([Certification, Article, Achievement, Interest])