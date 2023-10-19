from rest_framework import permissions


class DoctorAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.get_user_permissions())
        return 'api.view_doctor' in request.user.get_user_permissions()
