from DataModels.AlbumModel import Album
from flask_restful import Resource
from helpers import create_response


def build_response_object(data):
    album_list = []
    for album in data:
        album_details = {"title": album.title,
                 "artist": album.artist.name,
                 "tracks": build_track_data(album),
                 "location": album.location,
                 "year": str(album.year)}
        album_list.append(album_details)
    return album_list


def build_track_data(album):
    track_list = []
    for track in album.tracks:
        track = {"title": track.title,
                 "location": track.location}
        track_list.append(track)
    return track_list


class Albums(Resource):
    def get(self):
        data = Album.objects().all()
        return build_response_object(data)


class AlbumByName(Resource):
    def get(self, title):
        data = Album.objects(title=title).all()
        if len(data) > 0:
            return build_response_object(data)
        else:
            return create_response("No album with title: '{0}'".format(title), 404)

