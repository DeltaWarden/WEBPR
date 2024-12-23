from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from recipes.models import (
    Task,
    Tag,
    User,
)


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        fields = (
            'username',
            'id',
            'fio',
            'password',
        )
        model = User


class ReadUserSerializer(UserSerializer):
    class Meta:
        fields = (
            'username',
            'id',
            'fio',
        )
        model = User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'color')
        model = Tag


class DefaultTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'deadline',
        )


class TaskSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=False)
    author = UserSerializer()
    doer = UserSerializer()

    class Meta:
        fields = (
            'id',
            'pub_date',
            'tag',
            'text',
            'status',
            'author',
            'doer',
            'name',
        )
        model = Task


class CreateTaskSerializer(serializers.ModelSerializer):
    tag = PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=False)

    class Meta:
        fields = (
            'tag',
            'text',
            'doer',
            'author',
            'name',
        )
        model = Task

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task

    def validate(self, data):
        if self.context['request'].method == 'POST':
            data.pop('user', None)
        return data

    def to_representation(self, instance):
        return TaskSerializer(instance, context=self.context).data