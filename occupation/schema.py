import graphene
from graphene_django.types import DjangoObjectType

from occupation.models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = '__all__'


class Query(graphene.ObjectType):
    occupation = graphene.Field(OccupationType, id=graphene.Int())
    occupations = graphene.List(OccupationType)

    def resolve_occupation(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Occupation.objects.get(pk=id)

        return None

    def resolve_occupations(self, info):
        return Occupation.objects.all()


class OccupationInput(graphene.InputObjectType):
    name = graphene.String()
    company_name = graphene.String()
    position_name = graphene.String()
    hire_date = graphene.Date()
    fire_date = graphene.Date()
    salary = graphene.Int()
    fraction = graphene.Int()
    base = graphene.Int()
    advance = graphene.Int()
    by_hours = graphene.Boolean()


class CreateOccupation(graphene.Mutation):
    class Arguments:
        input = OccupationInput(required=True)

    occupation = graphene.Field(OccupationType)

    @staticmethod
    def mutate(cls, root, info, input):
        occupation = Occupation()
        occupation.name = input.name
        occupation.company_name = input.company_name
        occupation.position_name = input.position_name
        occupation.hire_date = input.hire_date
        occupation.fire_date = input.fire_date
        occupation.salary = input.salary
        occupation.fraction = input.fraction
        occupation.base = input.base
        occupation.advance = input.advance
        occupation.by_hours = input.by_hours
        occupation.save()

        return CreateOccupation(occupation=occupation)


class Mutation(graphene.ObjectType):
    create_occupation = CreateOccupation.Field()