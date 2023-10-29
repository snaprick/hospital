from django.contrib.auth.models import Permission
from rest_framework import permissions


class DoctorAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return 'api.view_doctor' in request.user.get_user_permissions()


class RoleBasedPermissionsMixin:
    """
    Role based permissions for authorization system
    """
    # You'll need to either set these attributes,
    # or override `get_action_permissions()`
    action_permissions = None

    def get_action_permissions(self):
        """
        Match the list of permissions that this view requires.
        You can specify permissions for each action by overriding method
        """
        self.action_permissions = None

    def get_permissions(self):
        self.get_action_permissions()  # Get role based permissions
        assert isinstance(self.action_permissions, list), (
                'Expected a `List` type of self.action_permissions '
                'but received a `%s`'
                % type(self.action_permissions)
        )
        return super().get_permissions()  # Overriding existing method of APIView


class HasPermissionByAuthenticatedUserRole(permissions.BasePermission):
    """
    Role based access
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if len(view.action_permissions) == 0:
                return True
            for permission in view.action_permissions:
                if has_perm(permission, request.user):
                    return True
        return False


def has_perm(perm, user):
    return user.is_active and perm in get_user_permissions(user)


def get_user_permissions(user):
    if user.is_superuser:
        return Permission.objects.values_list('codename', flat=True)

    return user.user_permissions.values_list('codename', flat=True) | Permission.objects.filter(
        group__user=user).values_list('codename', flat=True)
