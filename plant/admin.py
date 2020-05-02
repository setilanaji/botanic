from django.contrib import admin
from .models import Plant, Garden, Category, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


class PlantAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = 'name', 'local', 'date_added'
    list_filter = 'date_added',
    fields = ['name', 'local', 'synonym', 'slug', 'characteristic', 'gardens', 'image', 'date_added']
    readonly_fields = 'date_added', 'slug'

    def save_model(self, request, obj, form, change):
        obj.save()

        for afile in request.FILES.getlist('photos_multiple'):
            obj.photos.create(image=afile)


class GardenAdmin(admin.ModelAdmin):
    list_display = 'name', 'date_added'
    list_filter = 'name',
    fields = ['name', 'slug', 'desc', 'image', 'location_long', 'location_lat', 'date_added']
    readonly_fields = 'date_added', 'slug'


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'description', 'date_added',
    list_filter = 'name', 'date_added'
    fields = ['name', 'slug', 'description', 'plants', 'image', 'date_added']
    readonly_fields = 'date_added', 'slug'

# class BotanicAdmin(admin.ModelAdmin):
#     list_display = 'name', 'date_added', 'address'
#     list_filter = 'date_added',
#     fields = ['name', 'description', 'date_added', 'address', 'image', 'website']


admin.site.register(Plant, PlantAdmin)
admin.site.register(Garden, GardenAdmin)
# admin.site.register(Botanic, BotanicAdmin)
admin.site.register(Category, CategoryAdmin)
