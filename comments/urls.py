from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDeleteView

app_name = 'comments'

urlpatterns = [
    # List and create comments
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),

    # Retrieve, update, and delete comments
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-retrieve-update-delete'),
]
