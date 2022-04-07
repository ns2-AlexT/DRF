"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView

from userapp.views import UserModelViewSet
# from noteapp.views import ProjectModelViewSet, ToDoNoteViewSet
from noteapp.views import ProjectModelViewSet, ToDoNoteModelViewSet

# from noteapp.views import ProjectModelViewSet, ToDoNoteListAPIView, ToDoNoteCreateAPIView

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', ToDoNoteModelViewSet)

# router.register('users', UserViewSet, basename='users')
# router.register('notes', ToDoNoteViewSet, basename='notes')

'''
Schema for swagger
'''
schema_for_documentation = get_schema_view(
    openapi.Info(
        title='To do app',
        description='To do desk',
        default_version='0.1',
        contact=openapi.Contact(email='todoapp@mail.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),

    # path('swagger/', schema_for_documentation.with_ui('swagger')),
    path('swagger<str:format>', schema_for_documentation.without_ui()),
    path('redoc/', schema_for_documentation.with_ui('redoc')),

    path('graphql/', GraphQLView.as_view(graphiql=True)),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/list/', ToDoNoteListAPIView.as_view()),
    # path('api/create/', ToDoNoteCreateAPIView.as_view()),
    # path('api/upd/<int:pk>/', ToDoNoteUpdateAPIView.as_view()),
    # path('api/del/<int:pk>/', ToDoNoteDestroyAPIView.as_view()),
    # path('api/det/<int:pk>/', ToDoNoteRetrieveAPIView.as_view()),
    path('', TemplateView.as_view(template_name='index.html'))
]
