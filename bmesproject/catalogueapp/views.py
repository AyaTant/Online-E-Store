from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from catalogueapp import catalogue_service
# Create your views here.
def catalogue(request, category_slug='all-categories',brand_slug='all-brands'):
    assert isinstance(request,HttpRequest)
    if request.method == "POST":
        return render (
            request,
            'catalogueapp/index.html',
            {
                'title':'Product Page',
                'year':datetime.now().year,
            }
        )
    else:
        page_object = catalogue_service.fetch_products(request,category_slug,brand_slug)
        return render(
            request,
            'catalogueapp/index.html',
            {
                'title':'Product Page',
                'year':datetime.now().year,
                'page_object':page_object,
            }
        )

def product_detail(args):
    return render()
