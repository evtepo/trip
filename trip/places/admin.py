from django.contrib import admin

from .models import Hotels, City, Country

# Register your models here.
admin.site.register(Hotels)
admin.site.register(City)
admin.site.register(Country)