from django.urls import path
from webapp import views


urlpatterns = [
    path('',
        views.index,
        name='webapp.index'),
    path('login',
        views.login,
        name='webapp.login'),
    path('results',
        views.results,
        name='webapp.results'),
    path('checkin',
        views.checkin,
        name='webapp.checkin'),
    path('checkins',
        views.checkins,
        name='webapp.checkins'),
]

