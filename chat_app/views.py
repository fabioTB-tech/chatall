from django.shortcuts import render
from .forms import SendMessage
from .models import Chat
from users.models import CustomUser

# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST.get('msg')
        if message:
            form = Chat.objects.create(user=request.user, msg=message)
            form.save()
    
    msg = Chat.objects.all()
    return render(request, 'home.html', { 'messages': msg })