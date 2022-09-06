from django.contrib import admin
from . import models
from .models import Banner ,AsideBanner


# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'active']


    class Meta:
        model = Banner
# class BannerAside(admin.ModelAdmin):
#     list_display = ['title', 'image', 'active']


#     class Meta:
#         model = AsideBanner


admin.site.register(Banner, BannerAdmin)
# admin.site.register(AsideBanner,BannerAside)