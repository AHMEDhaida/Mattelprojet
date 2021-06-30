import django_filters
from .models import Installation

class InstallationFilter(django_filters.FilterSet):
    class Meta:
        model = Installation
        fields = '__all__'
        exclude = ['date_installe', 'date_update', 'author', 'equipement_installe','mac']