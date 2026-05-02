from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendMessage
from .models import Chat
from users.models import CustomUser, Galeria, Perfil
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
def home(request):
    if request.method == 'POST':
        message = request.POST.get('msg')
        if message:
            form = Chat.objects.create(user=request.user, msg=message)
            form.save()
    
    profiles = Perfil.objects.all()
    msg = Chat.objects.all()
    return render(request, 'home.html', { 'messages': msg, 'profiles': profiles })


@login_required
def galery(request):
    profiles = Perfil.objects.all()
    galeria = Galeria.objects.all()
    return render(request, 'galery.html', {'galeria': galeria, 'profiles': profiles})


@login_required
def post_like(request, post_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    post = get_object_or_404(Galeria, id=post_id)
    user = request.user

    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': post.likes.count(),
    })