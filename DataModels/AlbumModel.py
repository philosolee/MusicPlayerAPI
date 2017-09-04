from config import MONGO_DATABASE, MONGO_SERVER
from mongoengine import *
connect(MONGO_DATABASE)


class Album(Document):
    title = StringField(required=True)
    artist = ReferenceField('Artist')
    year = DateTimeField(required=False)
    tracks = ListField(ReferenceField('Track'))
    location = StringField(required=True)


