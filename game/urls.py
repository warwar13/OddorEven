from home.models import *
from django.contrib.auth.models import User
from django.urls import include, path
from . import views

app_name = 'game'

urlpatterns = [

    path('', views.index,name='home'),

]
