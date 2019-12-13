from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from reporter.models import Counties, Incidences


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'shops/index.html'


def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def incidence_data(request):
    incidences = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidences, content_type='json')
