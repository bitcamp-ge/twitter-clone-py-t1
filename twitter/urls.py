from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path('', include('hashtags.urls')),
    path('', include('posts.urls')),  
    path("", include("comments.urls")),
    path("filters/", include('filters.urls'))
]
