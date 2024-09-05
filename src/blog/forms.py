from django import forms
from .models import Comment




class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ['name', 'email', 'body']

      widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'placeholder': 'Enter your comment',
                'class': 'form-control',
                'rows': 4
            }),
        }