from .views import FollowView, FollowersViewSet, FollowingViewSet, PostView, FeedViewSet
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'follows', FollowView, 'follows')
router.register(r'posts', PostView, 'posts')



urlpatterns = [
    path('', include(router.urls)),
    path('followers/<int:pk>/', FollowersViewSet.as_view({'get': 'list'}), name='followers'),
    path('following/<int:pk>/', FollowingViewSet.as_view({'get': 'list'}), name='following'),
    path('feed/<int:pk>/', FeedViewSet.as_view({'get': 'list'}), name='feed'),
]

