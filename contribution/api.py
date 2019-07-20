from .models import Group, UserGroup, Contribution
from rest_framework import generics, permissions, filters
from .serializers import GroupSerializer, UserGroupSerializer, ContributionSerializer

# GroupApi
class GroupApi(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ["name"]
    
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)