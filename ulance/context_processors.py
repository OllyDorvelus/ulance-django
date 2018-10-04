from services.models import CategoryModel

def categories(request):
    parent_categories = CategoryModel.objects.filter(is_parent=True)
    sub_categories = CategoryModel.objects.filter(is_parent=False)
    return {'parent_categories': parent_categories, 'sub_categories': sub_categories}




