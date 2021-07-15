from django.contrib import admin
from .models import Flower


class FlowerAdmin(admin.ModelAdmin):

    list_display = ('name', 'species_name', 'family_name', 'description', 'slug')
    list_filter = ['name', 'species_name']
    search_fields = ['name', 'species_name']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Flower)
