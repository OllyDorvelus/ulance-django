from django.shortcuts import render
from django.forms import model_to_dict
from django.http import JsonResponse
from services.models import CategoryModel

def index(request):
    parent_categories = CategoryModel.objects.filter(is_parent=True)
    sub_categories = CategoryModel.objects.filter(is_parent=False)
    context = {"sub_categories": sub_categories, "parent_categories": parent_categories}
    return render(request, "base.html", context)