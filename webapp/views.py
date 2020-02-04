from django.shortcuts import render
from locations.connectors.foursquare import fs


def index(request):
    return render(request, 'index.html')


def results(request):
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')

    if lat and lon:
        print(fs.search_venues(lat, lon))

    return render(request, 'results.html')
