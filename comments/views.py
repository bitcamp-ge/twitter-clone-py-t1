from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from django.shortcuts import get_object_or_404
from posts.models import Post
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def get_queryset(self):
        content_type = self.request.query_params.get('content_type')
        object_id = self.request.query_params.get('object_id')
        if content_type and object_id:
            queryset = Comment.objects.filter(content_type=content_type, object_id=object_id)
        else:
            queryset = Comment.objects.all()
        return queryset
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        # Get the post_id from the URL kwargs
        post_id = self.kwargs.get('post_id')
        
        # Retrieve the associated post based on the post_id
        associated_post = get_object_or_404(Post, id=post_id)

        # Set the post reference when creating the comment
        serializer.save(author=self.request.user, content_object=associated_post)