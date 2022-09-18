from dataclasses import fields
from pyexpat import model
from django import forms
from .models import comments, video

class VideoForm(forms.ModelForm):
    class Meta:
        model=video
        fields=['name','video','description']


class VisitorsComment(forms.ModelForm):
    class Meta:
        model=comments
        fields=['visitorscomment']
        widgets = {
            'visitorscomment': forms.TextInput(attrs={'class':'col-sm-4'})
        }