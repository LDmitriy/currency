from django.contrib import admin
from django.urls import path

from currency import views as currency_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ContactUs/', currency_views.contactus)
]
