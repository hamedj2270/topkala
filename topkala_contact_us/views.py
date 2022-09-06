from django.shortcuts import render

from topkala_settings.models import SiteSettings
from .models import ContactUs
# Create your views here.
from topkala_contact_us.forms import ContactForm


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')

        ContactUs.objects.create(full_name=full_name, email=email, subject=subject, text=text, is_read=False)
        contact_form = ContactForm()

    setting = SiteSettings.objects.first()
    context = {
        'contact_form': contact_form,
        'setting': setting
    }
    return render(request, 'contact_us/contact_us_page.html', context)
