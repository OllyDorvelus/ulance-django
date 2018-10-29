from profiles.models import MajorModel, SkillModel, SchoolModel
from django_filters import FilterSet
import django_filters

class MajorFilter(FilterSet):
    major = django_filters.CharFilter(lookup_expr='icontains', field_name='major_name')

    class Meta:
        model = MajorModel
        fields = ['major',]

class SkillFilter(FilterSet):
    skill = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = SkillModel
        fields = ['skill',]

class SchoolFilter(FilterSet):
    school = django_filters.CharFilter(lookup_expr='icontains', field_name='school_name')

    class Meta:
        model = SchoolModel
        fields = ['school',]