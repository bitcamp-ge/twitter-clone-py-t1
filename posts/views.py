from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Hashtag
from .serializers import PostSerializer, HashtagSerializer



class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class HashtagView(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer