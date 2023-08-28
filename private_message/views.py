from telnetlib import STATUS
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.db.models import Q
from rest_framework.authentication import TokenAuthentication
from .models import PrivateMessage
from .serializers import PrivateMessageSerializer

class PrivateMessageList(viewsets.ModelViewSet):
    serializer_class = PrivateMessageSerializer
    # authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = PrivateMessage.objects.filter(Q(sender=user) | Q(recipient=user))
        else:
            queryset = PrivateMessage.objects.none()
        return queryset.order_by('-timestamp')
    
    def perform_create(self, serializer):
        current_user = self.request.user
        check_user = serializer.validated_data['recipient']
        print(check_user)
        print(current_user)

        if current_user != check_user:
            print(current_user != check_user)
            return Response({'detail': 'Sender must match the authenticated user.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(sender=current_user)
# class PrivateMessageListView(APIView):
#     def get(self, request):
#         messages = PrivateMessage.objects.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('-timestamp')
#         serializer = PrivateMessageSerializer(messages, many=True)
#         return Response(serializer.data)

# class SendPrivateMessage(APIView):
#     def post(self, request):
#         serializer = PrivateMessageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(sender=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

