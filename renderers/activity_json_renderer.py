from rest_framework import renderers


class ActivityJSONRenderer(renderers.JSONRenderer):
    media_type = 'application/activity+json'
