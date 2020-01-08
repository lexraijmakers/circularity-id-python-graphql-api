import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import PieceOfClothing as PieceOfClothingModel


class PieceOfClothing(MongoengineObjectType):
    class Meta:
        model = PieceOfClothingModel
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_pieces = MongoengineConnectionField(PieceOfClothing)
    piece = graphene.Field(PieceOfClothing)


schema = graphene.Schema(query=Query, types=[PieceOfClothing])
