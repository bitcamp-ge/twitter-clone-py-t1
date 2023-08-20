from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import PostFilter, HashtagFilter , UserFilter
from posts.serializers import PostSerializer
from hashtags.serializers import HashtagSerializer
from posts.models import Post
from hashtags.models import Hashtag
from django.contrib.auth.models import User
# Create your views here.

class PostSearchView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilter
    search_fields = ['content']

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = UserFilter
    search_fields = ['username']

class HashtagSearchView(generics.ListAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = HashtagFilter
    search_fields = ['tag']
