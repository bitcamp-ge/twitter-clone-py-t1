from rest_framework import serializers
from .models import Post
from hashtags.serializers import HashtagSerializer


class PostSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = ["content", "hashtags"]

