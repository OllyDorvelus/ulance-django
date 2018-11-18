from services.models import ServiceModel, CategoryModel, ReviewModel
from django_filters import FilterSet
import django_filters

class ServiceFilter(FilterSet):
    service = django_filters.CharFilter(lookup_expr='icontains', field_name='name')
    category = django_filters.CharFilter(lookup_expr='icontains', field_name='category__name')

    class Meta:
        model = ServiceModel
        fields = ['service', 'category',]

# class SkillFilter(FilterSet):
#     skill = django_filters.CharFilter(lookup_expr='icontains', field_name='name')
#
#     class Meta:
#         model = SkillModel
#         fields = ['skill',]
#
# class SchoolFilter(FilterSet):
#     school = django_filters.CharFilter(lookup_expr='icontains', field_name='school_name')
#
#     class Meta:
#         model = SchoolModel
#         fields = ['school',]