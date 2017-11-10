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


# class SigninForm(AuthenticationForm):
#     username = UsernameField(
#         max_length=254,
#         widget=forms.TextInput(
#             attrs={
#                 'autofocus': True,
#                 'class': 'form-control'
#             }),
#     )
#     password = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class': 'form-control',
#             }
#         ),
#     )
#
#     def confirm_login_allowed(self, user):
#         if not user.is_active:
#             raise forms.ValidationError(
#                 _("계정이 활성화되지 않았습니다."),
#                 code='inactive',
#             )

class SigninForm(forms.Form):
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
