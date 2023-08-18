from django.urls import path, include
from rest_framework import routers
from . views import HashtagView



router  = routers.DefaultRouter()
router.register(r'hashtags', HashtagView)


urlpatterns = [
    path('', include(router.urls)),
    
]