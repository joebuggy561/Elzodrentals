from django.contrib import admin
from .models import CarCategories, Products

class CarCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('vehicle_type', )}
    list_display = ('vehicle_type', 'slug')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_model', 'product_sit', 'product_transmission', 'product_doors', 'product_price_day', 'product_price_week', 'product_price_month', 'category')
    prepopulated_fields = {'slug' : ('product_name', )}


admin.site.register(CarCategories, CarCategoriesAdmin)
admin.site.register(Products, ProductAdmin)
