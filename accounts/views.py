from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from rest_framework.views import APIView

from .serializers import UserSerializer
from .models import User

from django.shortcuts import get_object_or_404

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            user.set_password(request.data["password"])
            user.save()
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key,
                "user": serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username = request.data["username"])
        
        if not user.check_password(request.data["password"]):
            # If the password doesnt match we return 404 NOT FOUND
            return Response(
                {"detail": "Not found."}, 
                status = status.HTTP_404_NOT_FOUND
            )
        
        token, created = Token.objects.get_or_create(user = user)
        serializer = UserSerializer(instance = user)
        
        return Response({
            "token" : token.key, 
            "user": serializer.data
        })
        
class ProfileView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username = username)
        user_data = dict(UserSerializer(instance = user).data)
        
        # We dont want to give away our password hash
        user_data.pop("password")
        
        return Response(user_data)

class SetBioView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data={"bio": request.data["bio"]}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "user": serializer.data
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)