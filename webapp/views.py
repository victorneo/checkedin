from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as loginuser
from django.shortcuts import render, redirect
from locations.models import Location
from locations.connectors.foursquare import fs


@login_required
def index(request):
    checkedin = False
    if request.session.get('checked-in'):
        checkedin = True
        request.session['checked-in'] = None

    return render(request, 'index.html', {'checkedin': checkedin})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            loginuser(request, user)
            return redirect('webapp.index')
        else:
            return render(request, 'login.html',
                          {'failed': True, 'username': username})


@login_required
def results(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    results = []

    if lat and lon:
        results = fs.search_venues(lat, lon)

    return render(request, 'results.html',
                  {'results': results})


@login_required
def checkin(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    name = request.GET.get('name')
    address = request.GET.get('address')

    user = request.user
    location = Location(user=user, lat=float(lat), lon=float(lon),
                        name=name, address=address)

    location.save()
    request.session['checked-in'] = True
    return redirect('webapp.index')


@login_required
def checkins(request):
    user = request.user
    start = request.GET.get('start', 0)
    next_count = start + 50
    locations = Location.objects.filter(user=user)[start:start+50]
    return render(request, 'checkins.html',
                  {'start': start, 'next_count': next_count,
                  'locations': locations})
