from django.urls import path, include
from rest_framework import routers
from . views import HashtagView
# from posts.views import PostListCreateView



router  = routers.DefaultRouter()
router.register(r'hashtags', HashtagView)
# router.register(r'posts', PostListCreateView)



urlpatterns = [
    path('', include(router.urls)),
]
