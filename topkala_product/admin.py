from django.contrib import admin
from . import models
from .models import Product, ProductGallery


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'image', 'active', 'image']

    # list_filter = ['title', 'price']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
