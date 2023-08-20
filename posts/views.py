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
        hashtags_data = self.request.data.get('hashtags') 
        post = serializer.save(user=self.request.user)

        if hashtags_data:
            for hashtag_name in hashtags_data:
                hashtag = Hashtag.objects.get_or_create(name=hashtag_name)
                post.hashtags.add(hashtag[0])  
                

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
