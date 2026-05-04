from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/', views.galery, name='galery'),
    path('galery/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.post_like, name='post_like'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/<int:feedback_id>/like/', views.like_feedback, name='like_feedback'),
]