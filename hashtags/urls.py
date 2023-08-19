from django.urls import path
from .views import HashtagListCreateView, HashtagDetailView



urlpatterns = [
    path('hashtags/', HashtagListCreateView.as_view(), name='hashtag-list'),
    path('hashtags/<int:pk>/', HashtagDetailView.as_view(), name='hashtag-detail'),
]