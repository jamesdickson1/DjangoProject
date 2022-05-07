from django import forms
from .models import Comments

class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
