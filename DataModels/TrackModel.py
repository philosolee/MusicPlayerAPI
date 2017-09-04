from config import MONGO_DATABASE, MONGO_SERVER
from mongoengine import *
connect(MONGO_DATABASE, host=MONGO_SERVER)


class Track(Document):
    title = StringField(required=True)
    year = StringField(required=False)
    genre = StringField(required=False)
    track_number = IntField(required=False)
    location = StringField(required=True)
    album = ReferenceField('Album')
    artist = ReferenceField('Artist')


