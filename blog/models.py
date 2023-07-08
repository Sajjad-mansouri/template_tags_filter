from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

class Post(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=100,unique=True)
	author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
	text=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def save(self,*args,**kwargs):
		self.slug=slugify(self.title)
		super().save(*args,**kwargs)
	def __str__(self):
		return self.title


