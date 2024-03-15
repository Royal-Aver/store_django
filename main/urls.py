from django.urls import path

from main.views import index, about, contact_info, delivery_pay_info

app_name = 'main'

urlpatterns = [
  path('', index, name='index'),
  path('about/', about, name='about'),
  path('contact-info/', contact_info, name='contact_info'),
  path('delivery-pay-info/', delivery_pay_info, name='delivery_pay_info'),
  ]
