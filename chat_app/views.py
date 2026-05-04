from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SendMessage
from .models import Chat, Feedback
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
def post_detail(request, post_id):
    post = get_object_or_404(Galeria, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


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


def feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        if feedback:
            form = Feedback.objects.create(user=request.user, feedback=feedback)
            form.save()
            return redirect('feedback')
    
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})


@login_required
@require_POST
def like_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    user = request.user

    if feedback.likes.filter(id=user.id).exists():
        feedback.likes.remove(user)
        liked = False
    else:
        feedback.likes.add(user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'likes_count': feedback.likes.count(),
    })
