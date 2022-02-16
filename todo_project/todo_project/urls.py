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
from rest_framework.routers import DefaultRouter

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/list/', ToDoNoteListAPIView.as_view()),
    # path('api/create/', ToDoNoteCreateAPIView.as_view()),
    # path('api/upd/<int:pk>/', ToDoNoteUpdateAPIView.as_view()),
    # path('api/del/<int:pk>/', ToDoNoteDestroyAPIView.as_view()),
    # path('api/det/<int:pk>/', ToDoNoteRetrieveAPIView.as_view()),
]
