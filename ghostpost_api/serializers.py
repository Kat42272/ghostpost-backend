from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = [
      'id',
      'choice_type',
      'body',
      'upVotes',
      'downVotes',
      'postDate',
      'totalVotes',
    ]
