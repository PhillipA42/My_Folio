from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Project, Service, Resume, Education, Experience
# Create your views here.

class HomeView(TemplateView):
    template_name ='pages/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['featured_projects'] = Project.objects.filter(featured=True)[:3]
        return ctx

class AboutView(TemplateView):
    template_name='pages/about.html'

class ResumeView(TemplateView):
    template_name='pages/resume.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['resume'] = Resume.objects.first()
        ctx['education'] = Education.objects.all()
        ctx['experience'] = Experience.objects.all()
        return ctx

class ServiceView(ListView):
    template_name = 'pages/services.html'
    model = Service
    context_object_name= 'services'

class PorfolioView(ListView):
    template_name = 'pages/portfolio.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all()
        