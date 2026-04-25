from django import forms
from .models import Chat
from users.models import CustomUser

class SendMessage(forms.ModelForm):
    user = CustomUser.username
    
    class Meta:
        model = Chat
        fields = ['msg']