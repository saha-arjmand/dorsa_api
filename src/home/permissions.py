from rest_framework.permissions import BasePermission


class OnlyAdminCanSee(BasePermission):

    message = 'permission denied, you not admin user'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user

    def has_object_permission(self, request, view, obj):
        if str(request.user) == 'admin':
            return True
        else:
            return False