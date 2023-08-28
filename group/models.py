from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#from accounts.models import User



    

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='groups_joined')
    admins = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='groups_admins', blank=False)

#     class Meta:
#         permissions = [
#             ('can_manage_group', 'Can manage group'),
#         ]

# def your_view_function(request, group_id):
#     # Get the authenticated user
#     admin_user = request.user

#     # Check if the user has the required permission
#     if admin_user.has_perm('your_app_name.can_manage_group'):
#         group = Group.objects.get(pk=group_id)  # Replace 'group_id' with the actual group ID
#         group.admins.add(admin_user)
#         # ... additional logic for managing the group ...
#     else:
#         # User doesn't have permission to manage the group
#         pass
