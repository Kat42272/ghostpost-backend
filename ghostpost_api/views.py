from .models import Post

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  @action(detail=False, methods=['post'])
  def boasts(self, request):
    boasts = Post.objects.filter(choices=True).order_by('-postDate')
    serializer = self.get_serializer(boasts, many=True)
    return Response(serializer.data)

  @action(detail=False, methods=['post'])
  def roasts(self, request):
    roasts = Post.objects.filter(choices=True).order_by('-postDate')
    serializer = self.get_serializer(roasts, many=True)
    return Response(serializer.data)

  @action(detail=False)
  def sortedTotal(self, request):
    posts = Post.objects.all()
    posts = sorted(posts, key=lambda post: post.total, reverse=True)
    serializer = self.get_serializer(posts, many=True)
    return Response(serializer.data)

  @action(detail=True, methods=['post'])
  def upVote(self, request, pk=None):
    post = self.get_object()
    post.upVotes += 1
    post.save()
    return Response({"status": post.upVotes})

  @action(detail=True, methods=['post'])
  def downVote(self, request, pk=None):
    post = self.get_object()
    post.downVotes += 1
    post.save()
    return Response({"status": post.downVotes})