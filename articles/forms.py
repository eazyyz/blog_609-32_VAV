from django import forms
from . import models

class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumbnail']
        labels = {
            'title': 'Title',
            'body': 'Text',
            'thumbnail': 'Thumbnail',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write article title', 'class': 'form-control mb-3'}),
            'body': forms.Textarea(attrs={'placeholder': 'Write article title', 'class': 'form-control mb-3'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }