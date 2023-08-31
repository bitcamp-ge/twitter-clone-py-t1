from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from hashtags.models import Hashtag
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from . permissions import IsOwnerOrReadOnly
import re


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    def perform_create(self, serializer):
        post = serializer.save(user=self.request.user)
        
        hashtags_data = self.extract_hashtags(post.content)  
        if hashtags_data:
            new_content = post.content
            for hashtag_name in hashtags_data:
                new_content = new_content.replace(hashtag_name, f'\n{hashtag_name}')
            post.content = new_content.strip()

            for hashtag_name in hashtags_data:
                hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_name)  
                post.hashtags.add(hashtag) 
        
        return post

    def extract_hashtags(self, content):
        return re.findall(r'#\w+', content)  




