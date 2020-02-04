from django.urls import path
from webapp import views


urlpatterns = [
    path('',
        views.index,
        name='webapp.index'),
    path('results',
        views.results,
        name='webapp.results'),
]

