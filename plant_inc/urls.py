"""plant_inc URL Configuration

The `urlpatterns` list routes URLs to views.
"""
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('catalogue/', include('catalogue.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'), 
    path('', RedirectView.as_view(url='catalogue/fruit-list')),
]