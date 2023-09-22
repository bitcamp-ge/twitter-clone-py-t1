from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



# class UsersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = '__all__'
    
# class AdminsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = '__all__'
