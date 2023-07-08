from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField(max_length=100,unique=True)
	author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
	text=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


