from rest_framework import permissions


class AllowAnyOnlyGet(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return permissions.IsAuthenticated
