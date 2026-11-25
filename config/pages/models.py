from django.db import models

# Create your models here.
class Resume(models.Model):
    summary = models.TextField()
    skills = models.JSONField(default=list, blank=True)
    updated_at =models.DateTimeField(auto_now=True)

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(null=True, blank=True)

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    tech_stack = models.JSONField(default=list, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering =['order']