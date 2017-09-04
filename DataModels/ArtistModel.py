import config
from mongoengine import *
connect(config.MONGO_DATABASE)


class Artist(Document):
    name = StringField(required=True)
    location = StringField(required=True)
    albums = ListField(ReferenceField('Album'))















