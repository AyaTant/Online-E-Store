from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from catalogueapp.models import Product

def fetch_products(request,category_slug,brand_slug):
    #fetch products from database
    products_list = Product.objects.filter(product_status=0) 
    #filtering the products
    if category_slug != 'all-categories'  and brand_slug != 'all-brands':
        products_list = Product.objects.filter(categories__slug=category_slug, brands__slug=brand_slug)
    if category_slug != 'all-categories' and brand_slug == 'all-brands':
        products_list = Product.objects.filter(categories__slug=category_slug)
    if category_slug == 'all-categories' and brand_slug !='all-brands':
        products_list=Product.objects.filter(brands__slug=brand_slug)
    
    #Paging the products
    page = request.GET.get('page',1)

    paginator = Paginator(products_list,9)
    try:
        page_object = paginator.page(page) # the page object will contain 1) the products per page, 2) the total number of pages for the list 3) the start and end pages
    except PageNotAnInteger:
        page_object = paginator.page(1)
    except EmptyPage:
        page_object = paginator.page(paginator.num_pages)
    return page_object