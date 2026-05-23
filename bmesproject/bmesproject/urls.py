from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include(('catalogueapp.urls','catalogueapp'),"catalogueappurls")),
    path('cart/',include(('cartapp.urls','cartapp'),'cartappurls')),
    path('checkout/',include(('checkoutapp.urls','checkoutapp'),'checkoutappurls')),
    path('admin/', admin.site.urls),
]
