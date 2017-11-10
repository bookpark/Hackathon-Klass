from django import forms

from .models import Assignment, SubmitAssignment


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


class SubmitAssignmentForm(forms.ModelForm):
    class Meta:
        model = SubmitAssignment
        fields = (
            'link',
            'context',
        )
        widgets = {
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
        }
