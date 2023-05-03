from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def Profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        first_name = request.user.first_name
        last_name = request.user.last_name
    else:
        username = None
    context = {
        'user_name': username,
        'email':email,
        'first_name':first_name,
        'last_name':last_name,
               }
    return render(request, 'profile.html', context)
