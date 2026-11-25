from django.db import models

# Create your models here.

class Certification(models.Model):
    name =models.CharField(max_length=200)
    issuer = models.CharField(max_length=150)
    date_obtained = models.DateField()
    credential_urel = models.URLField(blank=True)
    order =models.PositiveIntegerField(default=0)

    class Meta:
        ordering =['-date_obtained']

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date']

class Interest(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['order']
