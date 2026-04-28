from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendMessage
from .models import Chat
from users.models import CustomUser, Galeria
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST.get('msg')
        if message:
            form = Chat.objects.create(user=request.user, msg=message)
            form.save()
    
    msg = Chat.objects.all()
    return render(request, 'home.html', { 'messages': msg })


def galery(request):
    galeria = Galeria.objects.all()
    return render(request, 'galery.html', {'galeria': galeria})


@login_required
def post_like(request, pk):
    post = get_object_or_404(Galeria, id=pk)
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect(request.META.get('HTTP_REFERER'))