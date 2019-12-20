import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from users.models import User
from checkedin import settings


@pytest.mark.django_db
def test_webfinger_api():
    client = APIClient()
    url = '/.well-known/webfinger'
    resp = client.get(url, {'resource': 'acct:a@b.com'})
    assert resp.status_code == 404

    u = User(username='alpha', email='a@b.com', password='12345678')
    u.save()

    resp = client.get(url, {'resource': 'acct:a@'+ settings.DOMAIN_NAME})
    assert resp.status_code == 404

    resp = client.get(url, {'resource': 'acct:alpha@'+ settings.DOMAIN_NAME})
    assert resp.status_code == 200
    u.delete()


@pytest.mark.django_db
def test_user_api():
    client = APIClient()

    u = User(username='beta', email='a@b.com', password='12345678')
    u.save()

    url = '/users/'
    resp = client.get(url + 'a')
    assert resp.status_code == 404

    resp = client.get(url + 'beta')
    assert resp.status_code == 200

    u.delete()
