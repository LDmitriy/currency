from django.contrib import admin
from django.urls import path

from currency import views as currency_views

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('', currency_views.index),
    path('ContactUs/', currency_views.contactus),
    path('Rates/', currency_views.rates),
    path('Source/', currency_views.source),
    path('source/create/', currency_views.source_create)
]
