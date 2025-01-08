from django.core import validators as V
from django.db import models

from apps.pizza.managers import PizzaManager
from apps.pizza_shop.models import PizzaShopModel
from core.enums.regex_enum import RegexEnum

from core.models import BaseModel


class DaysChoices(models.TextChoices):
    MONDAY= 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY= 'Sunday'

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
        ordering = ('id',) # вказуєм сортування по замовчуванню(default)
    name = models.CharField(max_length=20, validators=[V.RegexValidator(RegexEnum.NAME.pattern, RegexEnum.NAME.msg)]) # (max_length=20, blank=True) = True дозволяє пусте поле
    price = models.IntegerField(validators=[V.MinValueValidator(1), V.MaxValueValidator(300)]) # (default=250) встановлює значення по замовчуванні, якщо не вказувати дані
    size = models.CharField(max_length=20) # (null=True) в крайньому випадку, зазвичай вказується для Foreign Key, коли потрібно зберегти дані, а foreign key вже немає
    day = models.CharField(max_length=9, choices=DaysChoices.choices)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')

    objects = PizzaManager()
