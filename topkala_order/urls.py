from django.urls import path

from . import views
from .views import add_user_order, user_open_order

urlpatterns = [
    path('add_user_order', add_user_order),
    path('user_open_order', user_open_order),
    path('request', views.send_request, name='request'),
    path('verify', views.verify, name='verify'),

]
