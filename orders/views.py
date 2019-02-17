from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, DetailView, ListView, FormView
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartModel
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class CartDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'Cart'
    template_name = 'cart.html'
    queryset = CartModel.objects.all()
    login_url = '/login/'

    def get_object(self):
        return CartModel.objects.get(user=self.request.user)
