# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404
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
    pagination_class = ProjectLimitOffsetPagination


# class ProjectViewSet(ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def create(self, request):
#         serializer_class = ProjectModelSerializer(data=request.data)
#         serializer_class.is_valid(raise_exception=True)
#         serializer_class.save()
#         headers = self.get_success_headers(serializer_class.data)
#         return Response(serializer_class.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     def get_success_headers(self, data):
#         try:
#             return {'Location': str(data[api_settings.URL_FIELD_NAME])}
#         except (TypeError, KeyError):
#             return {}
#
#     def list(self, request, *args, **kwargs):
#         project = Project.objects.all()
#         serializer = ProjectModelSerializer(project, many=True)
#         return Response(serializer.data)
#
#    def update(self, request, pk=None, partial_set=False, *args, **kwargs):
#        project = get_object_or_404(Project, pk=pk)
#        serializer = ProjectModelSerializer(project, data=request.data, partial=partial_set)
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)
#
#
#    def partial_update(self, request, pk=None, *args, **kwargs):
#        return self.update(request, pk, partial_set=True)
#
#    def retrieve(self, request, pk=None, *args, **kwargs):
#        user = get_object_or_404(Project, pk=pk)
#        serializer = ProjectModelSerializer(user)
#        return Response(serializer.data)
#
#    def destroy(self, request, pk=None, *args, **kwargs):
#        project = get_object_or_404(Project, pk=pk)
#        project.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)


class ToDONoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoNoteModelViewSet(ModelViewSet):
    queryset = ToDoNote.objects.all()
    serializer_class = ToDoNoteModelSerializer
    filterset_class = ToDoNoteFilter
    pagination_class = ToDONoteLimitOffsetPagination


# class ToDoNoteCreateAPIView(CreateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = ToDoNote.objects.all()
#    serializer_class = ToDoNoteModelSerializer
#
# class ToDoNoteListAPIView(ListAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = ToDoNote.objects.all()
#    serializer_class = ToDoNoteModelSerializer
#    filterset_class = ToDoNoteFilter
#    pagination_class = ToDONoteLimitOffsetPagination
#
# class ToDoNoteRetrieveAPIView(RetrieveAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = ToDoNote.objects.all()
#    serializer_class = ToDoNoteModelSerializer
#
# class ToDoNoteDestroyAPIView(DestroyAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = ToDoNote.objects.all()
#    serializer_class = ToDoNoteModelSerializer
#
# class BookUpdateAPIView(UpdateAPIView):
#    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#    queryset = ToDoNote.objects.all()
#    serializer_class = ToDoNoteModelSerializer
