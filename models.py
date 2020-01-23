from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    DateTimeField, ReferenceField, StringField,
)


class ImmutableProductData(Document):
    meta = {'collection': 'immutable_product_data'}
    sku = StringField()
    brand = StringField(required=True)


class Materials(Document):
    meta = {'collection': 'materials'}
    material_type = StringField(required=True)
    name = StringField(required=True)


class PieceOfClothing(Document):
    meta = {'collection': 'piece_of_clothing'}
    entry_created_on = DateTimeField(default=datetime.now)
    immutable_product_data = ReferenceField(ImmutableProductData)
    materials = ReferenceField(Materials)
