import django_filters
from .models import Likes

class LikeFilter(django_filters.FilterSet):
    class Meta:
        model = Likes
        fields =['postId','like_value']