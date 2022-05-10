from django.urls import path
from currency import views as currency_views

app_name = 'currency'

urlpatterns = [
    path('ContactUs/', currency_views.ContactUsList.as_view(), name='contact_us'),
    path('contactus_create/', currency_views.ContactUsCreate.as_view(), name='contactus_create'),
    path('Rates/', currency_views.RatesList.as_view(), name='rates'),
    path('Source/', currency_views.SourceList.as_view(), name='source'),
    path('source/create/', currency_views.SourceCreate.as_view(), name='source_create'),
    path('source/update/<int:pk>', currency_views.SourceUpdate.as_view(), name='source_update'),
    path('source/delete/<int:pk>', currency_views.SourceDelete.as_view(), name='source_delete')
]
