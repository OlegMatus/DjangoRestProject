from django.db import models

from core.models import BaseModel

class PizzaModel(BaseModel):
    class Meta:
        db_table = 'pizzas'
    name = models.CharField(max_length=100)
    price = models.FloatField()
    size = models.CharField(max_length=20)
