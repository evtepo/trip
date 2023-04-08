from django.contrib import admin

from .models import *


class HotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price_per_day', 'city')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'country')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'country')
    prepopulated_fields = {'slug': ('title',)}


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Hotels, HotelsAdmin)
admin.site.register(City, CitiesAdmin)
admin.site.register(Country, CountriesAdmin)