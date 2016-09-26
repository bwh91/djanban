
from django.conf.urls import url
from djanban.views import UpdateView, CreateView, DeleteView
from . import views

urlpatterns = [
    url(r'^project/(?P<id>\d+)/', views.projectdetail, name="projectdetail"),
    url(r'^update/(?P<story_pk>\d+)/$', UpdateView.as_view(), name="djanban_update"),
    url(r'^create/$', CreateView.as_view(), name="djanban_create"),
    url(r'^delete/(?P<story_pk>\d+)/$', DeleteView.as_view(), name="djanban_delete"),
    url(r'^', views.overview, name="overview"),


]
