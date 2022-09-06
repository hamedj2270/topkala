from django.contrib import admin

from topkala_slider.models import Slider


# Register your models here.

class SliderAdmin(admin.ModelAdmin):  # sliderfiled
    list_display = ['title', 'image', 'active']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
