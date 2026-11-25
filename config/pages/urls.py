from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('portfolio/', views.PorfolioView.as_view(), name='portfolio')
]