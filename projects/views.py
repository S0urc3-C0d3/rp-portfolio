from django.shortcuts import render
from projects.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request, "index.html", context)

def detail(request, pk):
    project = Project.objects.get(pk=pk)
    if(len(project.technology)== 0):
        project.technology = "There was no technology used"
        project.save()
    context = {"project":project}
    return render(request, "detail.html", context)