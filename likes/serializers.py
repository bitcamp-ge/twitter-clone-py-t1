from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['postId', 'like_from_User', 'like_value']
    def create(self, validated_data):
        user = validated_data['like_from_User']
        post = validated_data['postId']
        l_value = validated_data['like_value']

        exiting_like = Likes.objects.filter(like_from_User=user,postId=post,like_value=l_value).first()
        if exiting_like:
            raise serializers.ValidationError("This user already give like")
        return super().create(validated_data)


        