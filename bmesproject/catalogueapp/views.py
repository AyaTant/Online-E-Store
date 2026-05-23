from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from catalogueapp import catalogue_service
from cartapp import cart_service
# Create your views here.
def catalogue(request, category_slug='all-categories',brand_slug='all-brands'):
    assert isinstance(request,HttpRequest)
    if request.method == "POST":
        cart_service.add_to_cart(request) # adding items to the cart

        # the code to add items to the cart
        page_object = catalogue_service.fetch_products(request,category_slug,brand_slug)
        return render (
            request,
            'catalogueapp/index.html',
            {
                'title':'Product Page',
                'year':datetime.now().year,
                'page_object':page_object,
                'selected_category':category_slug,
                'selected_brand':brand_slug,
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
                'selected_category':category_slug,
                'selected_brand':brand_slug,
            }
        )

def product_detail(args):
    return render()
