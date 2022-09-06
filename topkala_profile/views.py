from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def Profile(request):

    context = {

    }
    return render(request,'profile.html',context)



def user_panel_menu_component(request : HttpRequest):
    return render(request,'',context)