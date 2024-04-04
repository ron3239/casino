from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from register_login.models import Player
from django.views.decorators.csrf import csrf_exempt


def index(request):
    context={
            'Login':'login'
    }

    return render(request=request,template_name='kazik_index\index.html')



