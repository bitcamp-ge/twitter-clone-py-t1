from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from hashtags.models import Hashtag

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        hashtags_data = self.request.data.get('hashtags')  # Get the hashtag IDs from the request
        post = serializer.save(user=self.request.user)

        if hashtags_data:
            for hashtag_id in hashtags_data:
                hashtag = Hashtag.objects.get(pk=hashtag_id)
                post.hashtags.add(hashtag)  # Associate the hashtags with the post


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
