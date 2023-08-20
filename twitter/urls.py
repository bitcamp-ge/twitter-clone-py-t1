from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.signup),
    path("login/", views.login),
    path("test/", views.test),
    path('', include('hashtags.urls')),
    path('', include('posts.urls')),  
    path("comments/", include("comments.urls",)),
]
