from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-us', views.aboutUs_view, name='about us'),
]