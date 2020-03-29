from unittest.mock import patch, MagicMock
import pytest


@patch('locations.connectors.foursquare.requests')
@patch('locations.connectors.foursquare.cache')
def test_foursquare_client(c, r):
    from locations.connectors.foursquare import FoursquareClient
    fc = FoursquareClient('123', '456')

    results = ['1']
    c.get.return_value = results

    venues = fc.search_venues(100, 200, 'abc')
    c.get.assert_called_once_with('location-100200abc')
    assert venues == results

    c.get.return_value = None

    resp = MagicMock()
    resp.status_code = 300
    r.get.return_value = resp

    with pytest.raises(Exception):
        fc.search_venues(100, 200, 'abc')

    resp.status_code = 200
    resp.json.return_value = {'response': {'venues': results}}
    r.get.return_value = resp

    venues = fc.search_venues(100, 200)

    assert venues == results
