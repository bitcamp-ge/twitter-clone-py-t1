from .views import FollowView, FollowersViewSet, FollowingViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'follows', FollowView, 'follow')
router.register(r'followers', FollowersViewSet, basename="followers")
router.register(r'following', FollowingViewSet, basename="following")



urlpatterns = [
    path('', include(router.urls)),
]
