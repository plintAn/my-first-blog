from django.shortcuts import render, get_object_or_404
from django.urls import path
from .models import Post  # Post 모델 가져오기
from . import views

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),  # views.post_detail에서 post_detail로 변경
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
