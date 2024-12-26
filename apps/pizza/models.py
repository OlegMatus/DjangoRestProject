from django.db import models

from apps.pizza_shop.models import PizzaShopModel
from core.models import BaseModel

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.CharField(max_length=20)
    pizza_shop = models.ForeignKey(PizzaShopModel, on_delete=models.CASCADE, related_name='pizzas')
