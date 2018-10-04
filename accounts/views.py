from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, ListView, FormView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404

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





