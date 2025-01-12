from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exists")
        return email
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email",required=True)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if "@" in username:
            try:
                user = User.objects.get(email=username)
                self.cleaned_data['username'] = user.username
            except User.DoesNotExist:
                raise forms.ValidationError("Email doesn't exists")
        else:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise forms.ValidationError("Username doesn't exists")
        return self.cleaned_data['username']
