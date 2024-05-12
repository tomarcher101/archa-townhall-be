from chat import models
from chat import serializers
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
  queryset = models.Post.objects.all().order_by('created_at').reverse()
  serializer_class = serializers.PostSerializer
