from mongoengine import connect

from models import PieceOfClothing

connect('cf-id-example', host='mongomock://localhost', alias='default')


def init_db():
    test_piece_of_clothing = PieceOfClothing(sku='SKU00001')
    test_piece_of_clothing.save()
