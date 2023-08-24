from .views import FollowView, FollowersViewSet, FollowingViewSet
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'follows', FollowView, 'follows')



urlpatterns = [
    path('', include(router.urls)),
    path('followers/<int:pk>/', FollowersViewSet.as_view({'get': 'list'}), name='followers'),
    path('following/<int:pk>/', FollowingViewSet.as_view({'get': 'list'}), name='following'),
]

