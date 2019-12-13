from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Incidences, Counties
from leaflet.admin import LeafletGeoAdmin


# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class CountiesAdmin(LeafletGeoAdmin):
    list_display = ('name_tag', 'area')

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Counties, CountiesAdmin)
