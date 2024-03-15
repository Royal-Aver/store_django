from django.shortcuts import render
from goods.models import Category

def index(request):
  context = {
    'title': "Gamer's Galaxy",
  }
  return render(request, 'main/index.html', context)

def about(request):
  context = {
    'title': 'О нас',
  }
  return render(request, 'main/about.html', context)


def contact_info(request):
  context = {
    'title': 'Контактная информация',
  }
  return render(request, 'main/contact_info.html', context)


def delivery_pay_info(request):
  context = {
    'title': 'Доставка и оплата',
  }
  return render(request, 'main/delivery_pay_info.html', context)
