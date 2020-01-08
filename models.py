from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    DateTimeField, StringField,
)


class PieceOfClothing(Document):
    meta = {'collection': 'piece_of_clothing'}
    sku = StringField()
    entry_created_on = DateTimeField(default=datetime.now)
