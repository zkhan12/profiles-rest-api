from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''allow user to update their own profile'''

    def has_object_permission(self, request, view, obj):
        '''check user is trying to edit their own profile'''
        if request.method in permissions.SAFE_METHODS:
            '''safe methods include GET but not PUT or PATCH'''
            return True

        '''only give the user permission if they are changing their own id'''
        return obj.id == request.user.id
