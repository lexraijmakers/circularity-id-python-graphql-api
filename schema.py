import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import \
    ImmutableProductData as ImmutableProductDataModel, \
    Materials as MaterialsModel, \
    PieceOfClothing as PieceOfClothingModel


class ImmutableProductData(MongoengineObjectType):
    class Meta:
        model = ImmutableProductDataModel
        interfaces = (Node,)


class Materials(MongoengineObjectType):
    class Meta:
        model = MaterialsModel
        interfaces = (Node,)


class PieceOfClothing(MongoengineObjectType):
    class Meta:
        model = PieceOfClothingModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    piece = MongoengineConnectionField(PieceOfClothing)


schema = graphene.Schema(query=Query, types=[ImmutableProductData, Materials, PieceOfClothing])
