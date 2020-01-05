from django.db import models

from core.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
