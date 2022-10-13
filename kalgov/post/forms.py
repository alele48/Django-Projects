from django import forms

from .models import PostJob


class PostJobForm(forms.ModelForm):

    class Meta:
        model = PostJob
        fields = ('title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }
