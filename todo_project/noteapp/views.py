from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDoNote
from .serializers import ProjectModelSerializer, ToDoNoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoNoteModelViewSet(ModelViewSet):
    queryset = ToDoNote.objects.all()
    serializer_class = ToDoNoteModelSerializer
