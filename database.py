from mongoengine import connect

from models import ImmutableProductData, Materials, PieceOfClothing

connect('cf-id-example', host='mongodb://localhost', alias='default')


def init_db():
    test_piece_of_clothing = PieceOfClothing(
        immutable_product_data=ImmutableProductData(sku="BBBBB", brand="ChangedClothing"),
        materials=Materials(material_type='LyoCell', name='LyoTex'))
    test_piece_of_clothing.immutable_product_data.save()
    test_piece_of_clothing.materials.save()
    test_piece_of_clothing.save()
