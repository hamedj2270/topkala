from django.shortcuts import render
from topkala_slider.models import Slider
from topkala_settings.models import SiteSettings


def home(request):
    context = {
        'Sliders': Slider.objects.all()

    }
    return render(request, 'home.html', context)


# render_partial_header
def render_partial_header(request):
    context = {}
    return render(request, 'base/header.html', context)


# render_partial_header
def render_partial_footer(request):
    site_setting = SiteSettings.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'base/footer.html', context)
