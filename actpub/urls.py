from django.urls import path
from actpub import views


urlpatterns = [
    path('.well-known/webfinger',
        views.WebFingerAPI.as_view(),
        name='webfinger'),
    path('users/<username>',
        views.UserAPI.as_view(),
        name='actpub-userapi'),
]
