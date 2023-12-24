from django.contrib import admin
from main.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description',)
