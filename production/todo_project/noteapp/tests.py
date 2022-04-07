from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer

from userapp.models import User
from noteapp.models import ToDoNote, Project
from userapp.views import UserModelViewSet
from noteapp.views import ProjectModelViewSet, ToDoNoteModelViewSet


class TestUsers(TestCase):
    def setUp(self) -> None:
        self.name_user = 'django'
        self.pass_user = 'geekbrains'
        self.mail_user = 'django_mail@mail.com'
        self.app_url = '/api/projects/'
        self.user_url = '/api/users/'
        self.admin = User.objects.create_superuser(self.name_user, self.mail_user, self.pass_user)
        self.data = {'name_of_project': 'test_project', 'link_to_repo': '', 'list_of_users': [self.admin.id]}
        self.user_data = {'first_name': 'test_user_!!!', 'e_mail': 'test_!!!@mail.com'}

    """
    testing APIRequestFactory get request for listing objects
    """

    def test_get_list_users(self):
        new_factory = APIRequestFactory()
        self.app_url = '/api/users/'
        t_request = new_factory.get(self.app_url)
        t_view = UserModelViewSet.as_view({'get': 'list'})
        t_response = t_view(t_request)
        self.assertEqual(t_response.status_code, status.HTTP_200_OK)

    """
    testing APIRequestFactory post request for creating object of todonote without auth
    """

    def test_post_create_todo_guest(self):
        new_factory = APIRequestFactory()
        t_request = new_factory.post(self.app_url, self.data, format='json')
        t_view = ToDoNoteModelViewSet.as_view({'post': 'create'})
        t_response = t_view(t_request)
        self.assertEqual(t_response.status_code, status.HTTP_401_UNAUTHORIZED)

    """
    testing APIRequestFactory post request for creating object of project with force auth
    """

    def test_post_create_user_admin(self):
        factory_project = APIRequestFactory()
        t_request = factory_project.post(self.app_url, self.data, format='json')
        force_authenticate(t_request, user=self.admin)
        t_view = ProjectModelViewSet.as_view({'post': 'create'})
        t_response = t_view(t_request)
        self.assertEqual(t_response.status_code, status.HTTP_201_CREATED)

    """
    testing APIClient get list of user
    """

    def test_get_users(self):
        client_connect = APIClient()
        user = User.objects.create(**self.user_data)
        response = client_connect.get(f'{self.user_url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
     testing APIClient get list of user under admin
     """

    def test_get_users_under_admin(self):
        client_connect = APIClient()
        user = User.objects.create(**self.user_data)
        client_connect.login(username=self.name_user, password=self.pass_user)
        response = client_connect.patch(f'{self.user_url}{user.id}/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_user = User.objects.get(id=user.id)
        self.assertEqual(new_user.first_name, self.user_data.get('first_name'))
        client_connect.logout()

    def tearDown(self) -> None:
        pass


"""
testing APITestCase 
"""


class TestProjects(APITestCase):
    def setUp(self) -> None:
        self.name_user = 'django'
        self.pass_user = 'geekbrains'
        self.mail_user = 'django_mail@mail.com'
        self.app_url = '/api/projects/'
        self.todo_url = '/api/notes/'
        self.admin = User.objects.create_superuser(self.name_user, self.mail_user, self.pass_user)
        self.data = {'name_of_project': 'test_project', 'link_to_repo': '', 'list_of_users': [self.admin.id]}
        self.user_data = {'first_name': 'test_user_!!!', 'e_mail': 'test_!!!@mail.com'}

    def test_get_list_of_projects(self):
        response = self.client.get(self.app_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_todo_mixer(self):
        todo = mixer.blend(ToDoNote)
        self.client.login(username=self.name_user, password=self.pass_user)
        response = self.client.patch(f'{self.todo_url}{todo.id}/', {'name_of_project': todo.name_of_project.id,
                                                                    'text_of_todo': 'test text',
                                                                    'author_of_todo': todo.author_of_todo.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        new_todo = ToDoNote.objects.get(id=todo.id)
        print(new_todo.id, '--', new_todo.text_of_todo, '--', new_todo.author_of_todo.username)
        self.assertEqual(new_todo.text_of_todo, 'test text')
        self.client.logout()
