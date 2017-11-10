from django import forms
from django.contrib.admin import widgets

from .models import Assignment


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment

        fields = (
            'title',
            'link',
            'context',
            'deadline',
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'context': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'deadline': forms.DateTimeInput()
        }
