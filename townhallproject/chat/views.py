from chat import models
from chat import serializers
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().order_by('created_at')
    serializer_class = serializers.PostSerializer
