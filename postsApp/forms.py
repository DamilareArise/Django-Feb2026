from django import forms
from .models import UserPost


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = UserPost
        fields = [
            'title',
            'content',
            'image',
            'category',
            'status'
        ]
    