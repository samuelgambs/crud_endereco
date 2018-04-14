from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=255)

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.PROTECT)
    name = models.CharField(max_length=255)

class Address(models.Model):
    state = models.ForeignKey(State,on_delete=models.PROTECT,verbose_name='Estado')
    city = ChainedForeignKey(
        City,
        chained_field="state",
        chained_model_field="state",
        show_all=False,
        auto_choose=True,
        sort=True,
        verbose_name='cidade')
    street = models.CharField(max_length=100, verbose_name='Endereço')
    zipcode = models.CharField(max_length=10,verbose_name='CEP',default='CEPCOMPLETO')