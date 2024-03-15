from django.urls import path

from goods.views import categories, products

app_name = 'goods'

urlpatterns = [
  path('search/', categories, name='search'),
  path('category/<slug:category_slug>/', categories, name='category'),
  path('product/<slug:product_slug>/', products, name='product'),
  ]