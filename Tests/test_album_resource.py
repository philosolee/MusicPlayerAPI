import pytest
from Tests.test_setup_fixtures import client
from helpers import json_of_response, url_encode_string


def test_get_all_albums_returns_200(client):
    response = client.get('/Albums')
    assert response.status_code == 200


def test_get_all_ablums_returns_album_object(client):
    response = client.get('/Albums')
    data = json_of_response(response)
    album = data[0]
    assert "title" in album.keys()
    assert "artist" in album.keys()
    assert "tracks" in album.keys()
    assert "location" in album.keys()
    assert "year" in album.keys()


def test_get_album_by_name_no_spaces(client):
    response = client.get('/Albums/Liars')
    data = json_of_response(response)
    assert data[0]["title"] == "Liars"


def test_get_album_by_name_with_spaces(client):
    response = client.get('/Albums/{0}'.format(url_encode_string("13 Blues for Thirteen Moons")))
    data = json_of_response(response)
    assert data[0]['title'] == "13 Blues for Thirteen Moons"


def test_get_album_by_name_doesnt_exist(client):
    response = client.get('/Albums/NonsenseTitle')
    assert response.data == b"No album with title: 'NonsenseTitle'"
    assert response.status_code == 404


if __name__ == "__main__":
    if __name__ == '__main__':
        pytest.main()
