from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaveLikes

ruter = DefaultRouter()
ruter.register(r'', SaveLikes, basename='likes')
urlpatterns = [
    path("", include(ruter.urls)),

]
