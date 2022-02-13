import graphene
import occupation.schema


class Query(occupation.schema.Query, graphene.ObjectType):
    pass


class Mutation(occupation.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)