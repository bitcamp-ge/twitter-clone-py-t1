from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.signup),
    path("login/", views.login),
    path("test/", views.test),
    path('', include('hashtags.urls')),
    path('', include('posts.urls')),  
]
