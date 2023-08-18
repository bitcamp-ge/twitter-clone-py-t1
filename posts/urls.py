from django.urls import path, include
from rest_framework import routers
from . views import PostView



router  = routers.DefaultRouter()
router.register(r'posts', PostView, 'post')


urlpatterns = [
    path('', include(router.urls)),
    
]