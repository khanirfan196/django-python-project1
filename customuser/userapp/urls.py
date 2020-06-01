from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.myhome, name='home-page'),
    path('register/', views.registration_view, name='registration-page'),
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout-page'),
    path('success/', views.success_view, name='success-page'),
]
