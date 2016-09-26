from django import forms
from .models import Story, Project


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = ('sprint',)

class ProjectForm(forms.ModelForm):




    class Meta:
        model = Project
        fields = ['name', 'description',]
