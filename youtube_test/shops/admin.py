from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Shop

# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')