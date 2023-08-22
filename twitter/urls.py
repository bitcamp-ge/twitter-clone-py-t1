from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accounts.urls")),
    path('', include('hashtags.urls')),
    path('', include('posts.urls')),  
    path("comments/", include("comments.urls",)),
    path("filters/", include('filters.urls'))
]
