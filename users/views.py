from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import CustomUser, Perfil, Galeria
from .forms import GaleriaForm, RegisterForm, LoginForm, EditProfile
from chat_app.models import Chat
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', { 'form': form }) 


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', { 'form': form })
    

def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request, pk):
    messages_count = Chat.objects.filter(user_id=pk).count()
    if request.user.is_authenticated:
        profile = Perfil.objects.get(user_id=pk)
        galeria = Galeria.objects.all()
        if request.method == 'POST':
            current_user_profile = request.user.perfil
            action = request.POST['follow']
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            current_user_profile.save()
                
        
        return render(request, 'accounts/profile.html', { 'count': messages_count, 'perfil': profile, 'galeria': galeria })
    else:
        messages.success(request, ('Você deve estar logado para entrar no seu perfil...'))
        return redirect('home')


def edit_profile(request):
    if request.user.is_authenticated:
        current_user = Perfil.objects.get(user_id=request.user.id)
        form = EditProfile(request.POST or None, request.FILES or None, instance=current_user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Perfil editado com sucesso!'))
            return redirect('home')
        
        return render(request, 'accounts/edit_pf.html', { 'form': form })
    else:
        messages.success(request, ('Você deve estar logado para visualizar esta página...'))
        return redirect('home')


@login_required
def add_post(request):
    if request.method == 'POST':
        img = request.FILES.get('image')
        desc = request.POST.get('desc')
        if img:
            post = Galeria.objects.create(user=request.user, image=img, description=desc)
            post.save()
            
    galeria = Galeria.objects.all()
    return render(request, 'accounts/add_post.html', {'galeria':galeria})

