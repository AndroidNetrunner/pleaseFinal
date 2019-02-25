from django import forms
from .models import Writing

class SongLyrics(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ['title','body']
