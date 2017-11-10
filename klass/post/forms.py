from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
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



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'type',
#             'title',
#             'link',
#             'context',
#             'is_active',
#         )