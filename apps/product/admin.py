from django.contrib import admin

from apps.product.models import Product, Category, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class Admin(admin.ModelAdmin):
    pass

