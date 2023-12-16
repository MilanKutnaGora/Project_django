from django.contrib import admin

from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')
    list_display_links = ('id', 'name')
    ordering = ('id',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
