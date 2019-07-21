from .models import Group, UserGroup, Contribution
from rest_framework import generics, permissions, status
from .serializers import GroupSerializer, UserGroupSerializer, ContributionSerializer
from rest_framework.response import Response
from django.db.models import Q

# Manage Groups
class GroupApi(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Filter groups
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            groups = Group.objects.filter(Q(isPublic=True) | Q(admin=self.request.user), name__icontains=search)
        else:
            groups = Group.objects.filter(Q(isPublic=True) | Q(admin=self.request.user))            
        return groups

    # get list of groups
    def get(self, request, *args, **kwargs):
        groups = self.get_queryset()
        serializer = self.serializer_class(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # create group and add admin user to group
    def post(self, request, *args, **kwargs):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            group = serializer.save(admin=request.user)
            group_user = UserGroup(group=group,user=request.user,slot=1)
            group_user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve Group List of Users
class UserGroupApi(generics.RetrieveAPIView):
    serializer_class = UserGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Get users from group id
    def get_queryset(self, pk):
        try:
            group = Group.objects.get(pk=pk,admin=self.request.user)
        except Group.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        users = UserGroup.objects.filter(group=group)
        return users

    # return list of users in a group
    def get(self, request, pk):
        users = self.get_queryset(pk)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
