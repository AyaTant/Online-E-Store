from bmesproject.bmesproject import settings
from catalogueapp.models import Brand, Category
def bmes_context(request):
    return {
        'site_name': settings.SITE_NAME,
        'categories':Category.objects.filter(category_status=0),
        'brands':Brand.objects.filter(brand_status=0),
        'selected_category':'all-categories',
        'selected_brand':'all-brands',
    }