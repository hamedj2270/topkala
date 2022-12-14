from django.contrib import admin

# Register your models here.
from topkala_contact_us.models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']
    # list_editable = ['is_read']
    search_fields = ['subject', 'text']


admin.site.register(ContactUs, ContactAdmin)
