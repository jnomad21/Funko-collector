import django_filters
from .models import Funko

class FunkoFilter(django_filters.FilterSet):
    class Meta:
        model = Funko
        fields = {
            'name': ['icontains'],
            'series': ['icontains']
        }
