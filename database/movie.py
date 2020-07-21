from database.db import db
import mongoengine_goodjson as gj


class Movie(gj.Document):
    name = db.StringField(required=True, unique=True)
    casts = db.ListField(db.StringField(), required=True)
    genres = db.ListField(db.StringField(), required=True)
