from rest_framework import serializers
from .models import Task


class TaskSerializerser(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
