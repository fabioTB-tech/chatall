from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('editprofile/', views.edit_profile, name='edit'),
    path('post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('people/', views.people, name='people'),
]