from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # Include all fields in the API
        read_only_fields = ['timestamp']  # Make timestamp read-only
