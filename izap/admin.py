

from django.contrib import admin
from izap.models import Address
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
	"""docstring for AddresAdmin"""
	list_display = ['id','zipcode','state','city','street']
	formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 40,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }


	
admin.site.register(Address, AddressAdmin)
