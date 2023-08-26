from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LikeSerializer
from .models import Likes
from .filters import LikeFilter


class SaveLikes(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSerializer
    filterset_class = LikeFilter
    filter_backends = [DjangoFilterBackend]

    # this function we need to remove previouse like orders if we have oposide like value
    def create(self, request, *args, **kwargs):
        post_id = request.data.get('postId')
        user_id = request.data.get('like_from_User')

        existing_with_True = Likes.objects.filter(postId=post_id, like_from_User=user_id, like_value = True).first()
        existing_with_False = Likes.objects.filter(postId=post_id, like_from_User=user_id, like_value = False).first()
        if existing_with_True:
            existing_with_True.delete()
        elif existing_with_False:
            existing_with_False.delete()
        return super().create(request, *args, **kwargs)