from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/', views.galery, name='galery'),
    path('post/<int:post_id>/like/', views.post_like, name='post_like'),
]