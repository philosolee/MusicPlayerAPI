from config import MONGO_SERVER, MONGO_DATABASE
from mongoengine import *
connect(MONGO_DATABASE, host=MONGO_SERVER)


class Artist(Document):
    name = StringField(required=True)
    location = StringField(required=True)
    albums = ListField(ReferenceField('Album'))















