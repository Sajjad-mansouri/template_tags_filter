from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone
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
	fields=['title','text']

	def form_valid(self,form):
		object=form.save(commit=False)
		object.author=self.request.user
		object.save()
		return HttpResponseRedirect(self.success_url)

class PostDelete(DeleteView):
	model=Post
	template_name='blog/post-delete.html'
	success_url=reverse_lazy('post-list')


class Simple(TemplateView):
	template_name='blog/simple.html'
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['name']='admin'
		context['timezone']=timezone.now()
		return context
