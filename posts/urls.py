from django.urls import path
from .views import PostListCreateView, PostDetailView


app_name = 'posts'

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]