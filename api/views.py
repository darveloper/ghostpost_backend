from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('total_votes')
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, id=None):
        post = Post.objects.get(id=id)
        post.upvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'upvotes': post.upvotes
        })
    
    @action(detail=True, methods=['post'])
    def downvote(self, request, id=None):
        post = Post.objects.get(id=id)
        post.downvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'downvotes': post.downvotes
        })

