from rest_framework import serializers
from .models import Post
from hashtags.serializers import HashtagSerializer


class PostSerializer(serializers.ModelSerializer):
    # hashtags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["user", "title", "content", "hashtags"]
