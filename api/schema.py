import graphene
from graphene_django import DjangoObjectType
from .knowledge.models import Profile

# Types
class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "name", "username")



# Mutations

class UpdateProfileMutation(graphene.Mutation):
    # Usable arguments on mutation
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        username = graphene.String()

    # Receives a type
    profile = graphene.Field(ProfileType)

    def mutate(self, info, id, name, username):
        profile = Profile.objects.get(pk=id)
        profile.name = name
        profile.username = username
        profile.save()
        return UpdateProfileMutation(profile=profile)
    

class DeleteProfileMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()

    def mutate(self, info, id):
        profile = Profile.objects.get(pk=id)
        profile.delete()
        return DeleteProfileMutation(message="Profile deleted")

class CreateProfileMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String()
        username=graphene.String()

    profile = graphene.Field(ProfileType)
    def mutate(self, info, name, username):
        profile = Profile(name=name, username=username)
        profile.save()
        return CreateProfileMutation(profile=profile)


# Queries
class Query(graphene.ObjectType):
    hello = graphene.String(default_value='hello')
    profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.ID())

    def resolve_profiles(self, info):
        return Profile.objects.all()

    def resolve_profile(self, info, id):
        return Profile.objects.get(pk=id)

# Mutations
class Mutation(graphene.ObjectType):
    create_profile = CreateProfileMutation.Field()
    delete_profile = DeleteProfileMutation.Field()
    update_profile = UpdateProfileMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


