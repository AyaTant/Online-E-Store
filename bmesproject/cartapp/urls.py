from django.urls import path
from . import views

app_name = 'cartapp'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
]