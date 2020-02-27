from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
from django.test import Client
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
