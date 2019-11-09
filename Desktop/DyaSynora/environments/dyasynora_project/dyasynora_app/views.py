from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt

from .models import Project
from .models import Activity

def projects(request):
    latest_project_list = Project.objects.order_by('-date_created')[:5]
    context = {'latest_project_list': latest_project_list}
    return render(request, 'dyasynora_app/projects.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'dyasynora_app/detail.html', {'project': project})

def activity(request, project_id):
    response = "You're looking at an activity of project %s."
    return HttpResponse(response % project_id)

# returns query set object containing a dictionary
def projects_json(request):
    return JsonResponse({
        'projects' : list(Project.objects.values())
    })

# returns query set object containing a dictionary
def activities_json(request):
    return JsonResponse({
        'activities' : list(Activity.objects.values())
    })

@csrf_exempt
def new_project(request):
    project_name = request.POST['project_name']
    project_description = request.POST['project_description']
    project_cost = request.POST['project_cost']
    project = Project(project_name = project_name, project_description = project_description, project_cost = project_cost)
    project.save()
    return JsonResponse({
        'id' : project.id,
        'project_name' : project.project_name,
        'project_description' : project.project_description,
        'project_cost' : project.project_cost
    })

@csrf_exempt
def new_activity(request):
    activity_name = request.POST['activity_name']
    duration = request.POST['duration']
    activity = Activity(activity_name = activity_name, duration = duration)
    project.save()
    return JsonResponse({
        'id' : activity.id,
        'activity_name' : activity.activity_name,
        'duration' : activity.duration
    })

@csrf_exempt
def delete_project(request,id):
    if request.method == 'DELETE':
        to_delete = Project.objects.filter(id=id)
        to_delete.delete()
    return JsonResponse({'message':"deleted!"}, safe=False)

@csrf_exempt
def update_project(request, id):
    if request.method == 'PUT':
        updated_project = Project.objects.get(id=id)
        input = QueryDict(request.body)
        print(input)
        project_name = input.get('project_name')
        project_description = input.get('project_description')
        project_cost = input.get('project_cost')
        updated_project.project_cost = project_cost
        updated_project.save()
        response = {
            'id' : updated_project.id,
            'project_name' : updated_project.project_name,
            'project_description' : updated_project.project_description,
			'project_cost': updated_project.project_cost
        }
        return JsonResponse(response, safe= False)
