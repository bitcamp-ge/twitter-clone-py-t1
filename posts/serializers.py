from rest_framework import serializers
from .models import Post
from hashtags.serializers import HashtagSerializer
from likes.serializers import LikeSerializer
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True, required=False)
    comments = CommentSerializer(many=True, read_only=True, required=False)
    likes = LikeSerializer(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ["content", "hashtags", "comments", "likes"]

  