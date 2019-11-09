from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.http import JsonResponse

from django.conf import settings
# Each class is table in database

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_img = models.ImageField(default="default.png", blank=True, null=True)
    project_description = models.TextField() # Unrestricted version of CharField
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed
    project_creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # if a user is deleted, also delete their projects
    project_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name

class Activity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # if a project is deleted, also delete its activities
    activity_name = models.CharField(max_length=100)
    duration = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now) # actual timezone function is passed

    def __str__(self):
        return self.activity_name
