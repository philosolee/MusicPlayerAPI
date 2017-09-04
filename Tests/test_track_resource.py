import pytest
from Tests.test_setup_fixtures import client
from helpers import json_of_response, url_encode_string


def test_get_tracks_returns_200(client):
    response = client.get('/Tracks')
    assert response.status_code == 200


def test_get_tracks_contains_track_object_keys(client):
    response = client.get('/Tracks')
    data = json_of_response(response)
    track = data[0]
    assert 'title' in track.keys()
    assert 'artist' in track.keys()
    assert 'album' in track.keys()
    assert 'location' in track.keys()
    assert 'year' in track.keys()


def test_get_track_by_title_with_spaces(client):
    response = client.get('/Tracks/{0}'.format(url_encode_string("Telluric In Transudate")))
    data = json_of_response(response)
    assert data[0]['title'] == "Telluric In Transudate"


def test_get_track_by_title_no_spaces(client):
    response = client.get('/Tracks/Nitinol')
    data = json_of_response(response)
    assert data[0]['title'] == "Nitinol"


def test_get_track_by_name_doesnt_exist(client):
    response = client.get('/Tracks/NonsenseTitle')
    assert response.data == b"No track with title: 'NonsenseTitle'"
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()