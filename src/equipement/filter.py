import django_filters
from .models import Equipement

class EquipementFilter(django_filters.FilterSet):
    class Meta:
        model = Equipement
        fields = '__all__'
        exclude = ['date_ajoute', 'author', 'nom']
