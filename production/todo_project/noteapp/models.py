from django.db import models

from userapp.models import User


class Project(models.Model):
    name_of_project = models.CharField('project name', max_length=32, unique=True)
    link_to_repo = models.URLField(blank=True)
    list_of_users = models.ManyToManyField(User)


class ToDoNote(models.Model):
    name_of_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_of_todo = models.TextField('text of note')
    data_time = models.DateTimeField(auto_now_add=True)
    data_time_update = models.DateTimeField(auto_now_add=True)
    author_of_todo = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active_of_todo = models.BooleanField(default=True)
