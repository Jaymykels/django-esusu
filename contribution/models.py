from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Groups
class Group(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    slots = models.IntegerField(default=0)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pass

# User's Group's
class UserGroup(models.Model):
    group = models.ForeignKey(Group, related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    month = models.CharField(max_length=100)
    inflow = models.FloatField(default=0)
    outflow = models.FloatField(default=0)
    pass

# Contributions
class Contribution(models.Model):
    source = models.ForeignKey(UserGroup, related_name='credits', on_delete=models.CASCADE)
    destination = models.ForeignKey(UserGroup, related_name='debits', on_delete=models.CASCADE)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    pass