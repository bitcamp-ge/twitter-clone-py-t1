from django.urls import path, include
from rest_framework import routers
from . views import PostView, HashtagView



router  = routers.DefaultRouter()
router.register(r'posts', PostView, 'post')
router.register(r'hashtags', HashtagView)


urlpatterns = [
    path('', include(router.urls)),
    
]