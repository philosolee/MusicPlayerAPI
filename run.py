from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from Resources.ArtistResource import Artists, ArtistsByName
from Resources.AlbumResource import Albums, AlbumByName
from Resources.TrackResource import Tracks, TrackByTitle

app = Flask(__name__)
api = Api(app)

api.add_resource(Artists, "/Artists", endpoint="all_artists")
api.add_resource(ArtistsByName, "/Artist/<string:name>", endpoint="artists_by_name")

api.add_resource(Albums, "/Albums", endpoint="all_albums")
api.add_resource(AlbumByName, "/Albums/<string:title>", endpoint="album_by_name")

api.add_resource(Tracks, "/Tracks", endpoint="all_tracks")
api.add_resource(TrackByTitle, "/Tracks/<string:title>", endpoint="track_by_title")

if __name__ == "__main__":
    app.run(debug=True)
