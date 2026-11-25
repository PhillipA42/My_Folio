from django.views.generic import ListView
from .models import Certification, Article, Achievement, Interest

class CertificationListView(ListView):
    model = Certification
    template_name = 'more/certifications.html'
    context_object_name = 'certifications'

class ArticleListView(ListView):
    model = Article
    template_name = 'more/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_published=True)

class AchievementListView(ListView):
    model = Achievement
    template_name = 'more/achievements.html'
    context_object_name = 'achievements'

class InterestListView(ListView):
    model = Interest
    template_name = 'more/interests.html'
    context_object_name = 'interests'