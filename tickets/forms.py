from django import forms
from .models import Bug, Feature


class BugPostForm(forms.ModelForm):

    class Meta:
        model = Bug
        fields = ('title', 'text')
