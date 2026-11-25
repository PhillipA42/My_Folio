from .models import NavItem

def navigation(request):
    return{
        'nav_items': NavItem.objects.filter(
            parent__isnull=True, is_active=True
        ).prefetch_related('children'),
    }