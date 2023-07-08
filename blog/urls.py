from django.urls import path
from . import views

urlpatterns=[
	path('',views.PostList.as_view(),name='post-list'),
	path('post/create/',views.PostCreate.as_view(),name='post-create'),
	path('post/detail/<slug:slug>/',views.PostDetail.as_view(),name='post-detail'),

]