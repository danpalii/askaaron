from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, SetPasswordForm
from .models import User

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-field-imput w-input'

class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length= 256, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'text-field-imput w-input'

class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    new_password1 = forms.CharField(
        strip=False,
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'New password',
        }),
    )
    new_password2 = forms.CharField(
        strip=False,
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'New password confirmation'
        }),
    )
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'text-field-imput w-input'

class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'text-field-imput w-input'

