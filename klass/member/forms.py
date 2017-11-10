from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ('password1', 'password2')
        for field in class_update_fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        self.user = authenticate(username=username, password=password)
        if not self.user:
            raise forms.ValidationError("계정 이름 또는 암호가 맞지 않습니다")
        else:
            setattr(self, 'login', self._login)
        return cleaned_data

    def _login(self, request):
        if self.user is not None:
            login(request, self.user)
