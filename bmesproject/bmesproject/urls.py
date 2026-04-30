from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include(('catalogueapp.urls','catalogueapp'),"catalogueappurls")),
    path('admin/', admin.site.urls),
]
