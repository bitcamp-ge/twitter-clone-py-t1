from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HashtagViewSet
from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'hashtags', HashtagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]