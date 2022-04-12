from django.core.management import BaseCommand

from userapp.models import User
from noteapp.models import Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        Project.objects.all().delete()

        User.objects.create_superuser('django', 'admin@test.com', 'geekbrains')

        # project_list = [
        #     {'name_of_project': 'Project 1', 'list_of_users': [1], 'link_to_repo': ''},
        #     {'name_of_project': 'Project 2', 'list_of_users': [1], 'link_to_repo': ''},
        #     {'name_of_project': 'Project 3', 'list_of_users': [1], 'link_to_repo': ''}
        # ]
        #
        # for item in project_list:
        #     Project.objects.create(**item)
