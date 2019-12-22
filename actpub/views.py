from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from checkedin.settings import DOMAIN_NAME
from users.models import User


class WebFingerAPI(APIView):
    def get(self, request):
        resource = request.query_params.get('resource', '')
        parts = resource.replace('acct:', '').split('@')
        username = parts[0]
        domain = parts[1]

        if domain != DOMAIN_NAME:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        resp = {
            'subject': resource,
            'links': [
                {'rel': 'self',
                 'type': 'application/activity+json',
                 'href': 'https://' + DOMAIN_NAME + '/users/'+ user.username}]
        }

        return Response(resp)


class UserAPI(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        url = 'https://' + DOMAIN_NAME + '/users/'+ user.username

        resp = {
            '@context': [
                'https://www.w3.org/ns/activitystreams',
                'https://w3id.org/security/v1'
            ],
            'id': url,
            'type': 'Service',
            'preferredUsername': user.username,
            'inbox': 'https://'+ DOMAIN_NAME + '/inbox',
            'followers': url + '/followers',
            'name': user.username,
            'publicKey': {
                'id': url + '#main-key',
                'owner': url,
                'publicKeyPem': user.public_key
            }
        }

        return Response(resp, content_type='application/activity+json')
