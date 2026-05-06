from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser, Perfil, Galeria

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


class EditProfile(forms.ModelForm):
    class Meta:
        model = Perfil 
        fields = ['avatar', 'bio']


class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ['description', 'image']
