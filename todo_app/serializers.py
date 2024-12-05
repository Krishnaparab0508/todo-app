from rest_framework import serializers
from .models import Task, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ["id", "timestamp", "title", "description", "due_date", "status", "tags"]

    def create(self, validated_data):
        tags_data = validated_data.pop("tags", [])
        task = Task.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            task.tags.add(tag)
        return task

    def update(self, instance, validated_data):
        tags_data = validated_data.pop("tags", [])
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return super().update(instance, validated_data)
