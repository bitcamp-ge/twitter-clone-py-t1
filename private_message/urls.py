from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

ruter = DefaultRouter()
ruter.register(r'conver_list', views.PrivateMessageList, basename='conver_list')
# ruter.register(r'conver_list1/', views.SendPrivateMessage, basename='conver_list1')

urlpatterns = [
    path('', include(ruter.urls)),
    # path('send/', views.PrivateMessageListView.as_view(), name='api-send-message'),
]