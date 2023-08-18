# from django.urls import path, include
# from rest_framework import routers
# from . views import PostListCreateView, PostDetailView

# router  = routers.DefaultRouter()
# router.register(r'posts', PostListCreateView, 'post')
# router.register(r'posts', PostDetailView)

# urlpatterns = [
#     path('', include(router.urls)),  
# ]

from django.urls import path
from .views import PostListCreateView, PostDetailView

app_name = 'posts'

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]