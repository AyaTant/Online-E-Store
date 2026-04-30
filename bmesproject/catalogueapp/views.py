from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
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
        return render(
            request,
            'catalogueapp/index.html',
            {
                'title':'Product Page',
                'year':datetime.now().year,
            }
        )

def product_detail(args):
    return render()
