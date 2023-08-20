from django_filters import rest_framework as filters

class PostFilter(filters.FilterSet):
    hashtags = filters.CharFilter(field_name='hashtags__tag', lookup_expr='icontains')
    user = filters.CharFilter(field_name='author__username', lookup_expr='icontains')

class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']

class HashtagFilter(filters.FilterSet):
    tag = filters.CharFilter(lookup_expr='icontains')
