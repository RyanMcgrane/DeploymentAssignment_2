from django.core import serializers
from django.http import HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Shop, Person
import json

# Create your views here.

longitude = -6.2603
latitude = 53.3498

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(
        distance=Distance('location', user_location)
    ).order_by('distance')[0:6]
    template_name = 'shops/nearByShops.html'


def index(request):
    template = 'shops/nearByShops.html'
    results = Shop.objects.all()
    jsondata = serializers.serialize('json', results)
    context = {
        'results': results,
        'jsondata': jsondata,
    }
    return render(request, template, context)


def getdata(request):
    results = Shop.objects.all()
    jsondata = serializers.serialize('json', results)
    return HttpResponse(jsondata)


def base_layout(request):
    template = 'shops/base.html'
    return render(request, template)


def shopMap(request):
    template = 'shops/shopMap.html'
    return render(request, template)


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')


home = Home.as_view()
