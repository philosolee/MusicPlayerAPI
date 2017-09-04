from flask_restful import Resource
from DataModels.ArtistModel import Artist
from helpers import create_response


class Artists(Resource):
    def get(self):
        result = Artist.objects().all().to_json()
        return create_response(result, 200)


class ArtistsByName(Resource):
    def get(self, name):
        result = Artist.objects(name=name).all().to_json()
        return create_response(result, 200)