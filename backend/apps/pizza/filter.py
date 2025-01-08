# from django.db.models import QuerySet
# from django.http import QueryDict
#
# from rest_framework.exceptions import ValidationError
#
# from apps.pizza.models import PizzaModel
from apps.pizza.models import PizzaModel, DaysChoices
from apps.pizza.serializers import PizzaSerializer

from django_filters import rest_framework as filters
from random import choices

# def filter_pizza(query: QueryDict)-> QuerySet:
#     qs = PizzaModel.objects.all()
#     for k,v in query.items():
#         match k:
#             case 'price_gt':
#                 qs = qs.filter(price__gt=v)
#             case 'price_lt':
#                 qs = qs.filter(price__lt=v)
#             case _:
#                 raise ValidationError({'detail':f'"{k}" not allowed'})
#
#     return qs


class PizzaFilter(filters.FilterSet):
    lt = filters.NumberFilter(fields=('price', 'size'), lookup_expr='lt')
    gt = filters.NumberFilter(fields=('price', 'size'), lookup_expr='gt')
    lte = filters.NumberFilter(fields=('price', 'size'), lookup_expr='lte')
    gte = filters.NumberFilter(fields=('price', 'size'), lookup_expr='gte')

    name_starts_with = filters.CharFilter(field_name='name', lookup_expr='startswith')
    name_ends_with = filters.CharFilter(field_name='name', lookup_expr='endswith')
    name_contains = filters.CharFilter(field_name='name', lookup_expr='contains')

    day_starts_with = filters.CharFilter(field_name='day', lookup_expr='startswith')
    day_ends_with = filters.CharFilter(field_name='day', lookup_expr='endswith')
    day_contains = filters.CharFilter(field_name='day', lookup_expr='contains')

    range = filters.RangeFilter(
        field_name='price')  # в query параметрах ми просто добавляєм min i max(range_min=2,range_max=100)
    price_in = filters.BaseInFilter(
        field_name='price')  # query параметрах вказуєм числові проміжки(price_in=30,35,1500)
    day = filters.ChoiceFilter('day',choices=DaysChoices.choices)
    # order = filters.OrderingFilter(fields=PizzaSerializer.Meta) # Сортує по всім полям
    order = filters.OrderingFilter(
        fields=(
            'id',
            'name',
            ('price', 'asd')# можна перейменувати поле для сортування
        )
    ) # order = name(asc),
      # order = -name(desc)
