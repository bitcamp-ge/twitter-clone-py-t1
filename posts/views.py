from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from hashtags.models import Hashtag
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        
        hashtags_data = self.request.data.get('hashtags') 
        post = serializer.save(user=self.request.user)

        if hashtags_data:
             for hashtag_name in hashtags_data:
                hashtag = Hashtag.objects.get_or_create(name=hashtag_name)
                post.hashtags.add(hashtag[0]) 
  
