import graphene
from django.db.models import Q
from django.shortcuts import get_object_or_404
from graphene import ObjectType
from graphene_django import DjangoObjectType


from noteapp.models import Project, ToDoNote
from userapp.models import User


class UserTypeDjango(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']


class ProjectTypeDjango(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoNoteTypeDjango(DjangoObjectType):
    class Meta:
        model = ToDoNote
        fields = '__all__'


class QueryGraphQl(ObjectType):
    get_request_user_by_name = graphene.List(UserTypeDjango, name=graphene.String())
    get_request_projects = graphene.List(ProjectTypeDjango)
    get_request_todonotes = graphene.List(ToDoNoteTypeDjango)
    check_user_by_id = graphene.Field(UserTypeDjango, id=graphene.ID())

    def resolve_get_request_projects(root, info):
        return Project.objects.all()

    def resolve_get_request_todonotes(root, info):
        return ToDoNote.objects.all()

    def resolve_get_request_user_by_name(root, info, name=None):
        if name:
            return User.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name))

    def resolve_check_user_by_id(root, info, id=None):
        if id:
            print(User)
            return get_object_or_404(User, id=id)

class UserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        id = graphene.ID()

    user_upd = graphene.Field(UserTypeDjango)

    @classmethod
    def mutate(cls, root, info, id, first_name):
        user_upd = User.objects.get(pk=id)
        user_upd.first_name = first_name
        user_upd.save()
        return UserMutation(user_upd=user_upd)


class Mutation(ObjectType):
    upd_user = UserMutation.Field()


schema_todo = graphene.Schema(query=QueryGraphQl, mutation=Mutation)
