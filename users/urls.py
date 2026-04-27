from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path(f'profile/<int:pk>', views.profile, name='profile'),
    path('editprofile/', views.edit_profile, name='edit'),
    path('post/', views.add_post, name='add_post'),
]