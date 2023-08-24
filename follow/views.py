from rest_framework import viewsets
from .serializers import FollowSerializer
from .models import Follow



class FollowView(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
           

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