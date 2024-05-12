from django.db import models

class Post(models.Model):
  content = models.CharField(max_length=200)
  poster_name = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.content