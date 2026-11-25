from django.urls import path
from . import views

urlpatterns = [
    path('certifications/', views.CertificationListView.as_view(), name='certifications'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('achievements/', views.AchievementListView.as_view(), name='achievements'),
    path('interests/', views.InterestListView.as_view(), name='interests'),
]