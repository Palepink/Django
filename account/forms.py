from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)
    email = forms.EmailField(label='email', widget=forms.EmailInput)

    class Meta:
        model = models.User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('密码错误')
        return cd['password2']