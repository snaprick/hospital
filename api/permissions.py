from rest_framework import permissions


class DoctorAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.get_user_permissions())
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
