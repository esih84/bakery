from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone', 'username', 'role']

    def clean_password2(self):
        data = self.cleaned_data
        if data['password2'] and data['password1'] and data['password2'] != data['password1']:
            raise forms.ValidationError('PLEASE CHECK THE PASSWORD')
        return data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class CostumerProfileUpdate(forms.ModelForm):
    class Meta:
        model = CostumerProfile
        fields = ['first_name', 'last_name', 'city', 'address']


class SellerProfileUpdate(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = ['first_name', 'last_name', 'city', 'address', 'bakeryPhone', 'Holiday', 'type']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['phone', 'username']

class LoginPhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']


class CodePhoneForm(forms.ModelForm):
    class Meta:
        model = CostumerProfile
        fields = ['verify_phone']