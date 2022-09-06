from django.contrib import admin
from topkala_settings.models import SiteSettings

# Register your models here.


class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']

    class Meta:
        model = SiteSettings


admin.site.register(SiteSettings, SettingAdmin)
