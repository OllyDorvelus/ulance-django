from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

User = get_user_model()


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, "loginform.html", {})


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, "registerform.html", {})





