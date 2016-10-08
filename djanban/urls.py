
from django.conf.urls import url
from djanban.views import UpdateView, CreateView, DeleteView, ProjectUpdateView, ProjectDeleteView, ProjectCreateView
from . import views

urlpatterns = [
    url(r'^project/update/(?P<project_pk>\d+)/$', ProjectUpdateView.as_view(), name="djanban_project_update"),
    url(r'^project/create/$', ProjectCreateView.as_view(), name="djanban_project_create"),
    url(r'^project/delete/(?P<project_pk>\d+)/$', ProjectDeleteView.as_view(), name="djanban_project_delete"),
    url(r'^project/(?P<id>\d+)/', views.projectdetail, name="projectdetail"),
    url(r'^update/(?P<story_pk>\d+)/$', UpdateView.as_view(), name="djanban_update"),
    url(r'^create/$', CreateView.as_view(), name="djanban_create"),
    url(r'^delete/(?P<story_pk>\d+)/$', DeleteView.as_view(), name="djanban_delete"),
    url(r'^', views.overview, name="overview"),


]
