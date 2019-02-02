from profiles.models import MajorModel, SkillModel, SchoolModel, ProfileModel
from django_filters import FilterSet
import django_filters


class MajorFilter(FilterSet):
    major = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = MajorModel
        fields = ['major',]


class SkillFilter(FilterSet):
    skill = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = SkillModel
        fields = ['skill',]


class SchoolFilter(FilterSet):
    school = django_filters.CharFilter(lookup_expr='icontains', field_name='name')

    class Meta:
        model = SchoolModel
        fields = ['school',]


class ProfileFilter(FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', field_name='user__username')
    first_name = django_filters.CharFilter(lookup_expr='icontains', field_name='first_name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', field_name='last_name')
   # school = django_filters.CharFilter(lookup_expr='iexact', field_name='educations')

    class Meta:
        model = ProfileModel
        fields = ['username', 'first_name', 'last_name',]