from django import forms
from .models import Story


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Story
        exclude = ('sprint',)
