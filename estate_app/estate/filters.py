from django_filters import rest_framework as filters
from .models import *

class Filter(filters.FilterSet):
    # filters = filters.ModelChoiceFilter(queryset=Filters.objects.all())
    type = filters.ChoiceFilter(choices=HOUSE_TYPES)
    heating = filters.ChoiceFilter(choices=HEATING_TYPES)
    fridge = filters.BooleanFilter()
    microwave = filters.BooleanFilter()
    washMachine = filters.BooleanFilter()
    oven = filters.BooleanFilter()
    conditioner = filters.BooleanFilter()
    router = filters.BooleanFilter()
    TV = filters.BooleanFilter()
    square = filters.RangeFilter()
    floor = filters.RangeFilter()
    floors = filters.RangeFilter()

    class Meta:
        model = Filters
        fields = [
            'fridge',
            'microwave',
            'washMachine',
            'oven',
            'conditioner',
            'router',
            'TV',
            'type',
            'heating',
            'square',
            'floor',
            'floors'
        ]

class AnnouncementFilter(filters.FilterSet):
    cost = filters.RangeFilter()
    address = filters.CharFilter()

    class Meta:
        model = Announcement
        fields = ['cost', 'address']