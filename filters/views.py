from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filters import PostFilter, UserFilter, HashtagFilter
from .serializers import PostSerializer, UserSerializer, HashtagSerializer
from .models import Post, User, Hashtag
# Create your views here.

class PostSearchView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilter
    search_fields = ['content']

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
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
