from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
# from django.urls import path, include
# from django.conf.urls import url
from django.conf import settings
from django.views.generic import TemplateView
from .views import signin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', views.RegistrationView.as_view(), name='register')
    
]