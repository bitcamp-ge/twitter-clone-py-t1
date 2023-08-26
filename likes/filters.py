from django_filters import rest_framework as djangoFilter
import django_filters
from .models import Likes

class LikeFilter(django_filters.FilterSet):
    # like_value = django_filters.BooleanFilter(field_name="like_value")
    class Meta:
        model = Likes
        fields =['postId','like_value']