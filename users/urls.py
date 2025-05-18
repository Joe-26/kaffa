from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signup_view, name='signup'),
    path('sign-in', views.signin_view, name='signin'),
    path('sign-out', views.signout_view, name='signout'),
    
    # API Testing through Postman
    path('api/get-users', views.getUsers, name='get-users'),
]