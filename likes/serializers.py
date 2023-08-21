from rest_framework import serializers
from .models import Likes

class LiseSerializer(serializers):
    class Meta:
        model = Likes
        fields = ['postId', 'like_from_User', 'like_value']

        