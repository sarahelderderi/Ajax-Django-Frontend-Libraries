from django.urls import path
from django.http import JsonResponse
from dyasynora_app import views

app_name = 'dyasynora_app'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.detail, name='detail'),
    path('projects.json', views.projects_json, name='list of projects'),
    path('activities.json', views.activities_json, name='list of activities'),
    path('new_project/', views.new_project, name='new project'),
    path('new_activity/', views.new_activity, name='new activity'),
    path('delete_project/<int:id>', views.delete_project, name='delete project'),
    path('update_project/<int:id>', views.update_project, name='update'),
]
