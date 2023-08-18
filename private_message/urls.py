from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.PrivateMessageList.as_view(), name='api-message-list'),
    path('send/', views.SendPrivateMessage.as_view(), name='api-send-message'),
]