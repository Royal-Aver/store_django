from django.contrib import admin
from goods.models import Category, Products

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}