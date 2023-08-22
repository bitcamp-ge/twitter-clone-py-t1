from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from hashtags.models import Hashtag


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        hashtags_data = self.request.data.get('hashtags') 
        post = serializer.save(user=self.request.user)

        if hashtags_data:

             for hashtag_name in hashtags_data:
                hashtag = Hashtag.objects.get_or_create(name=hashtag_name)
                post.hashtags.add(hashtag[0]) 

           

