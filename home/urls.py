from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import  views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.register,name='register'),

]
