from chat import models
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id', 'content', 'poster_name', 'created_at']
