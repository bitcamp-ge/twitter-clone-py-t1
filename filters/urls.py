
from django.urls import path


from .views import PostSearchView, HashtagSearchView, UserSearchView

urlpatterns = [
    path('posts/search/', PostSearchView.as_view(), name='post-search'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
    path('hashtags/search/', HashtagSearchView.as_view(), name='hashtag-search'),
]
