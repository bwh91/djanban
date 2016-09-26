from django.shortcuts import render
from .models import Story, Project
from fm.views import AjaxUpdateView, AjaxCreateView, AjaxDeleteView
from .forms import UpdateForm, ProjectForm

class UpdateView(AjaxUpdateView):
    model = Story
    form_class = UpdateForm
    pk_url_kwarg = 'story_pk'

class CreateView(AjaxCreateView):

    form_class = UpdateForm

class DeleteView(AjaxDeleteView):

    model = Story
    pk_url_kwarg = 'story_pk'

class ProjectUpdateView(AjaxUpdateView):
    model = Story
    form_class = ProjectForm
    pk_url_kwarg = 'project_pk'

class ProjectCreateView(AjaxCreateView):

    form_class = ProjectForm

class ProjectDeleteView(AjaxDeleteView):

    model = Project
    pk_url_kwarg = 'project_pk'

def overview(request):
    projects = Project.objects.all()
    return render(request, 'djanban/overview.html', {
        'projects': projects,
    })

def projectdetail(request, id):
    project = Project.objects.get(id=id)
    s = Project.objects.get(pk=id)
    stories = s.story_set.all()
    return render(request, 'djanban/project_detail.html', {
        'project': project, 'stories': stories,
    })
