from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import (PasswordChangeForm,ReadOnlyPasswordHashField)
from django.core.exceptions import ValidationError
# from .models import User


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

class SignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput({'placeholder': "Current password", 'id': "old_password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': "New password", 'id': "new_password1"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': "Confirm password", 'id': "new_password2"}))

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("Your current password was entered incorrectly. please try again")
        return old_password
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'is_active', 'is_superuser','is_staff')