from django.contrib import admin
from .models import Plant, Garden


class PlantAdmin(admin.ModelAdmin):
    list_display = 'name', 'family', 'local', 'garden', 'date_added'
    list_filter = 'family', 'garden', 'date_added'
    fields = ['name', 'family', 'local', 'synonym', 'characteristic', 'image', 'garden', 'date_added']


class GardenAdmin(admin.ModelAdmin):
    list_display = 'name', 'date_added'
    list_filter = 'date_added',
    fields = ['name', 'desc', 'date_added']


admin.site.register(Plant, PlantAdmin)
admin.site.register(Garden, GardenAdmin)
