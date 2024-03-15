from django.urls import path

from orders.views import create_orders

app_name = 'orders'

urlpatterns = [
  path('create-orders/', create_orders, name='create_orders'),
  ]

create_orders