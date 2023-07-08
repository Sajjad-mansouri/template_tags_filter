from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy
from .models import Post

class PostList(ListView):
	model=Post
	template_name='blog/post.html'


class PostDetail(DetailView):
	model=Post
	template_name='blog/post.html'


class PostCreate(CreateView):
	model=Post
	template_name='blog/post-create.html'
	success_url=reverse_lazy('post-list')
	fields=['title','slug','author','text']