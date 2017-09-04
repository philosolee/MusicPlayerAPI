import config
from mongoengine import *
connect(config.MONGO_DATABASE)


class Track(Document):
    title = StringField(required=True)
    year = StringField(required=False)
    genre = StringField(required=False)
    track_number = IntField(required=False)
    location = StringField(required=True)
    album = ReferenceField('Album')
    artist = ReferenceField('Artist')


