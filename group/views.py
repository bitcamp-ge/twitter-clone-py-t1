# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from django.views import View
# from rest_framework import viewsets
# from .serializer import GroupSerializer
# from .models import Group
# from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.authentication import TokenAuthentication





#from .pagination import TasksPagination
#from .filters import TaskFilter



# class GroupView(viewsets.ModelViewSet):
#     serializer_class = GroupSerializer
#     queryset = Group.objects.all()
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class UsersView(viewsets.ModelViewSet):
#     serializer_class = UsersSerializer
#     queryset = Users.objects.all()


# class AdminsView(viewsets.ModelViewSet):
#     serializer_class = AdminsSerializer
#     queryset = Admins.objects.all()




from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Group
from .serializers import GroupSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def is_group_admin(self, user, group):
        return user in group.admins.all()


    @csrf_exempt
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if not self.is_group_admin(request.user, instance):
            return Response({"detail": "You are not authorized to edit this group."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().update(request,args, kwargs)

    def partial_update(self, request, *args, kwargs):
        instance = self.get_object()

        if not self.is_group_admin(request.user, instance):
            return Response({"detail": "You are not authorized to edit this group."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().partial_update(request, *args, **kwargs)