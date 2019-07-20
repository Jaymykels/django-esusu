from .models import Group, UserGroup, Contribution
from rest_framework import generics, permissions
from .serializers import GroupSerializer, UserGroupSerializer, ContributionSerializer

# GroupApi
class GroupApi(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
        # serializer.validated_data['admin'] = self.request.user
        # return super().perform_create(serializer)