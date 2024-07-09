from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "description", "precio"]
    search_fields = ["name"]

admin.site.register(Product, ProductAdmin)