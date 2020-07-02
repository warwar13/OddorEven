from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from home.models import Profile
# Create your views here.

def index(request):
    get_balance = Profile.objects.get(user=request.user.id)
    balance = get_balance.balance
    context ={
        'balance':balance,
              }

    return render(request,'game/home.html', context)
