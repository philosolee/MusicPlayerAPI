from flask_restful import Resource
from DataModels.TrackModel import Track
from DataModels.AlbumModel import Album
from DataModels.ArtistModel import Artist
from helpers import create_response


def build_response_object(data):
    track_list = []
    for track_details in data:
        track_details = {"title": track_details.title,
                 "album": track_details.album.title,
                 "artist": track_details.artist.name,
                 "location": track_details.location,
                 "year": str(track_details.year)}
        track_list.append(track_details)
    return track_list


class Tracks(Resource):
    def get(self):
        data = Track.objects().all()
        return build_response_object(data)


class TrackByTitle(Resource):
    def get(self, title):
        data = Track.objects(title=title).all()
        return build_response_object(data)

