from django.shortcuts import render
from locations.connectors.foursquare import fs


def index(request):
    return render(request, 'index.html')


def results(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if lat and lon:
        results = fs.search_venues(lat, lon)

    return render(request, 'results.html',
                  {'results': results})

