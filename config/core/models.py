from django.db import models
from django.urls import reverse
# Create your models here.

class NavItem(models.Model):
    label = models.CharField(max_length=50)
    url_name = models.CharField(max_length=100, blank=True, help_text="Django URL name e.g 'home'")
    external_url = models.URLField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.label

    @property
    def has_children(self):
        return self.children.filter(is_active=True).exiats()
