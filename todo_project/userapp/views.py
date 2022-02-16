# from rest_framework.response import Response
# from rest_framework.generics import get_object_or_404
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins, viewsets

from .models import User
from .serializers import UserModelSerializer


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5


class UserModelViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = UserLimitOffsetPagination


# class UserViewSet(ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def list(self, request, *args, **kwargs):
#         user = User.objects.all()
#         serializer = UserModelSerializer(user, many=True)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None, partial_set=False, *args, **kwargs):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(user, data=request.data, partial=partial_set)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def partial_update(self, request, pk=None, *args, **kwargs):
#         return self.update(request, pk, partial_set=True)
#
#     def retrieve(self, request, pk=None, *args, **kwargs):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data)
