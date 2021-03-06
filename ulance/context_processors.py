from services.models import CategoryModel
from django.contrib.auth import get_user_model

User = get_user_model()


def categories(request):
    parent_categories = CategoryModel.objects.filter(is_parent=True)
    sub_categories = CategoryModel.objects.filter(is_parent=False)
    return {'parent_categories': parent_categories, 'sub_categories': sub_categories}


def user(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        return {'user': user}
    else:
        return {}





