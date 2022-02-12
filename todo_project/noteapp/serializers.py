from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project, ToDoNote


class ProjectModelSerializer(ModelSerializer):
    list_of_users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoNoteModelSerializer(ModelSerializer):
    name_of_project = serializers.StringRelatedField()
    author_of_todo = serializers.StringRelatedField()

    class Meta:
        model = ToDoNote
        fields = '__all__'
