from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db.models import Q
from .models import PrivateMessage
from .serializers import PrivateMessageSerializer


class PrivateMessageList(APIView):
    def get(self, request):
        messages = PrivateMessage.objects.filter(Q(recipient=request.user) | Q(sender=request.user)).order_by('-timestamp')
        serializer = PrivateMessageSerializer(messages, many=True)
        return Response(serializer.data)

class SendPrivateMessage(APIView):
    def post(self, request):
        serializer = PrivateMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
