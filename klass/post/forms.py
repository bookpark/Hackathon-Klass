from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {
            'context': '',
        }
        fields = (
            'context',
        )
        widgets = {
            'context': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'link',
            'context',
            'is_active',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'context': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
