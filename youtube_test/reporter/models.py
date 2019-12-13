from __future__ import unicode_literals
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models


# Create your models here.

class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.name

    # Converts the name incidencess to incidences on the admin site
    class Meta:
        verbose_name_plural = "Incidences"


class Counties(models.Model):
    osm_id = models.FloatField()
    name_tag = models.CharField(max_length=255)
    name_ga = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    alt_name = models.CharField(max_length=255)
    alt_name_g = models.CharField(max_length=255)
    logainm_re = models.CharField(max_length=255)
    osm_user = models.CharField(max_length=100)
    osm_timest = models.CharField(max_length=38)
    attributio = models.CharField(max_length=255)
    t_ie_url = models.CharField(max_length=33)
    area = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    epoch_tstm = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.name_tag

    class Meta:
        verbose_name_plural = "Counties"
