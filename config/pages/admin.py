from django.contrib import admin
from .models import Resume, Education, Experience, Service, Project

admin.site.register([Resume, Education, Experience, Service, Project])