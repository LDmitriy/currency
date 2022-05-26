from django.urls import path
from .accounts import views

app_name = 'accounts'

urlpatterns = [
    path('my_profile/', views.MyProfile.as_view(), name='my-profile'),
]
