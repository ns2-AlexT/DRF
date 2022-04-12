from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet, ViewSet

from .filter import ToDoNoteFilter, ProjectFilter
from .models import Project, ToDoNote
from .serializers import ProjectModelSerializer, ToDoNoteModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    # pagination_class = ProjectLimitOffsetPagination


class ToDONoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoNoteModelViewSet(ModelViewSet):
    queryset = ToDoNote.objects.all()
    serializer_class = ToDoNoteModelSerializer
    filterset_class = ToDoNoteFilter
    # pagination_class = ToDONoteLimitOffsetPagination

    # def destroy(self, request, pk=None, *args, **kwargs):
    #     todonote = get_object_or_404(ToDoNote, pk=pk)
    #     todonote.is_active_of_todo = False
    #     todonote.save()
    #     return Response(status.HTTP_200_OK)
