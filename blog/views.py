from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

class PostList(ListView):
	model=Post
	template_name='blog/post.html'


class PostDetail(DetailView):
	model=Post
	template_name='blog/post.html'