from rest_framework import viewsets
from .serializers import FollowSerializer
from .models import Follow
from .pagination import PostsPagination
from posts.models import Post
from posts.serializers import PostSerializer
from django.db.models import Q

class FollowView(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
           

class FollowersViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    def get_queryset(self):
        """
        This view should return a list of all the followers
        for the currently authenticated user.
        """
        user_pk = self.kwargs['pk'] 
        return Follow.objects.filter(following=user_pk)
    
class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    def get_queryset(self):
        """
        This view should return a list of all the followed users 
        from the currently authenticated user.
        """
        user_pk = self.kwargs['pk'] 
        return Follow.objects.filter(follower=user_pk)
    

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostsPagination

    def get_queryset(self):
        # Get the currently authenticated user
        user_pk = self.kwargs['pk']

        # Get the users being followed by the current user
        followed_users = Follow.objects.filter(follower=user_pk).values_list('following', flat=True)

        # Get the ten latest posts from the followed users
        latest_posts = Post.objects.filter(user__in=followed_users).order_by('-created_at')[:1000]

        return latest_posts

