from django.db import models

# Create your models here.

# class County(models.Model):
#     name = models.CharField(_('Name'), max_length=100, unique=True)

# class Municipality(models.Model):
#     county = models.ForeignKey(County, verbose_name=_('County'))
#     name = models.CharField(_('Name'), max_length=100)

# class Location(models.Model):
#     name = models.CharField(max_length=100)
#     county = models.ForeignKey(County, verbose_name=_('County'))
#     municipality = models.ForeignKey(Municipality,
#             verbose_name=_("Municipality"))

            
class Address(models.Model):


	
    street = models.TextField(max_length=20, verbose_name='Endereço',default='endereço')
    city = models.TextField(max_length=20, verbose_name='Cidade',default='cidade')
    province = models.TextField(max_length=20, verbose_name='Estado',default='BR')
    code = models.TextField(max_length=20, verbose_name='CEP',default='00000-000')
    class Meta:
         verbose_name = "Endereço"

