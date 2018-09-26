from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse


def login(request):
    return render(request, "loginform.html", {})


def register(request):
    return render(request, "registerform.html", {})