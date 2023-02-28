from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name="index"),
  path('posts/', views.posts, name="posts"),
  path('post/<slug:slug>', views.post, name="post"),
  path('createpost/', views.createpost, name="createpost"),
  path('readpost/', views.readpost, name="readpost"),
  path('updatepost/<slug:slug>', views.updatepost, name="updatepost"),
  path('deletepost/<slug:slug>', views.deletepost, name="deletepost"),
  path('send_email', views.sendEmail, name="sendemail")
]