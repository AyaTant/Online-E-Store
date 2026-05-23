from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
from cartapp import cart_service

# Create your views here.
def cart_detail(request):
    """Renders the cart page"""
    assert isinstance(request, HttpRequest)

    # Remove item from cart
    if request.method == "POST":
        cart_service.remove_from_cart(request)

    # Get cart items
    cart_items = cart_service.get_cart_items(request)

    # Calculate totals
    cart_total = sum(item.cart_item_total() for item in cart_items)

    cart_item_count = sum(item.quantity for item in cart_items)

    return render(
        request,
        'cartapp/cart_detail.html',
        {
            'title': 'Cart Page',
            'year': datetime.now().year,
            'cart_items': cart_items,
            'cart_total': cart_total,
            'cart_item_count': cart_item_count,
        }
    )