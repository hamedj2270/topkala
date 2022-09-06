from django.shortcuts import render
from .models import Banner, AsideBanner


# Create your views here.
def banner(request):
    baner = Banner.objects.all()
    context = {
        'baner': baner
    }
    return render(request, 'home.html', context)

def aside_banner(request):
    asbanner = AsideBanner.objects.all()
    context = {
        'asbanner':asbanner
    }
    return render(request,'base/aside.html',context)