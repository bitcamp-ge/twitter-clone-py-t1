from rest_framework import serializers
from .models import Post
from hashtags.serializers import HashtagSerializer
from comments.serializers import CommentSerializer
from likes.serializers import LikeSerializer



class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True, required=False)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
   

    class Meta:
        model = Post
        fields = ["content", "hashtags"]

  
