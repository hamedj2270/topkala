from django.urls import path
from .views import admin_page ,admin_page2

urlpatterns = [
    path('admin_page',admin_page),
    path('admin_page2',admin_page2),

]