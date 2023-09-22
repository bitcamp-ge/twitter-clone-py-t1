from django.urls import path,include
from .views import GroupViewSet
#from .views import GroupView
from rest_framework import routers


router = routers.DefaultRouter()
#router.register(r'',GroupView, 'groups' )
router.register(r'', GroupViewSet, 'groups')
# router.register(r'users',UsersView)
# router.register(r'admins',AdminsView)



urlpatterns = [
    path('', include(router.urls))
]