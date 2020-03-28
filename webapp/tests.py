from unittest.mock import patch
from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
from django.test import Client
from users.models import User
from locations.models import Location
import pytest


def test_index(client, admin_client):
    url = reverse('webapp.index')
    resp = client.get(url)
    assertRedirects(resp, reverse('webapp.login')+'?next='+url)

    resp = admin_client.get(url)
    assertTemplateUsed('index.html')


def test_login(client, admin_client):
    url = reverse('webapp.login')
    resp = client.get(url)
    assertTemplateUsed(resp, 'login.html')

    resp = client.post(url, {'username': 'asd', 'password': 'asd'})
    assertTemplateUsed(resp, 'login.html')
    assert resp.context.get('failed') == True

    resp = client.post(url, {'username': 'admin', 'password': 'password'})
    assertRedirects(resp, reverse('webapp.index'))


@patch('webapp.views.fs')
def test_results(fs, client, admin_client):
    url = reverse('webapp.results')

    results = ['1']
    fs.search_venues.return_value = results

    resp = admin_client.get(url)
    assertTemplateUsed(resp, 'results.html')
    assert resp.context.get('results') == []

    resp = admin_client.get(url, {'lat': 100, 'lon': 100})
    assertTemplateUsed(resp, 'results.html')
    assert resp.context.get('results') == results


def test_checkin(client, admin_client):
    url = reverse('webapp.checkin')

    data = {'name': 'Someplace', 'lat': 100, 'lon': 200, 'address': '123'}
    resp = admin_client.get(url, data)

    user = User.objects.get(username='admin')
    l = Location.objects.get(user=user)

    assert l.name == data['name']
    assert l.address == data['address']
    assert l.lat == float(data['lat'])
    assert l.lon == float(data['lon'])

    assertRedirects(resp, reverse('webapp.index'))


def test_checkins(client, admin_client):
    url = reverse('webapp.checkins')
    user = User.objects.get(username='admin')
    l = Location(user=user, name='Someplace', lat=100, lon=200,
                 address='Someplace St')
    l.save()

    resp = admin_client.get(url)
    assertTemplateUsed(resp, 'checkins.html')
    assert resp.context.get('locations')[0] == l
