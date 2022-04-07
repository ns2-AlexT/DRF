from django_filters import rest_framework as filters

from noteapp.models import ToDoNote, Project


class ProjectFilter(filters.FilterSet):
    name_of_project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name_of_project']


class ToDoNoteFilter(filters.FilterSet):
    name_of_project = filters.CharFilter(lookup_expr='name_of_project')

    class Meta:
        model = ToDoNote
        fields = ['name_of_project']
