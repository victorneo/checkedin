import requests
from django.conf import settings


class FoursquareClient(object):
    URL_PREFIX = 'https://api.foursquare.com/v2/'
    PLACES_SEARCH_API = URL_PREFIX + 'venues/search'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def search_venues(self, lat, lon):
        params = {'ll': str(lat) + ',' + str(lon),
                  'intent': 'checkin',
                  'client_id': self.client_id,
                  'client_secret': self.client_secret,
                  'limit': 50}

        resp = requests.get(self.PLACES_SEARCH_API, params=params)
        print(resp.content)
        if resp.status_code != 200:
            raise Exception('Foursquare Error')

        return resp.json()['response']['venues']


fs = FoursquareClient(settings.FOURSQUARE_CLIENT_ID,
        settings.FOURSQUARE_CLIENT_SECRET)
