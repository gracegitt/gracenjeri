from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .filters import *

from .models import *

from .forms import *
# Create your views here.

def index(request):
  posts = Post.objects.filter(active=True, featured=True)[0:3]

  context = {'posts' : posts}
  
  return render(request, "portfolio/index.html", context)


def post(request, slug):
  post = Post.objects.get(slug=slug)
  
  context = {'post' : post}
  
  return render(request, "portfolio/post.html", context)

def posts(request):
  posts = Post.objects.all()
  myfilter = PostFilter(request.GET, queryset=posts)
  posts = myfilter.qs

  page = request.GET.get('page')

  paginator = Paginator(posts, 3)

  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)
  context = {'posts' : posts, 'myfilter': myfilter}
  
  return render(request, "portfolio/posts.html", context)

#CRUD
@login_required(login_url='home')
def createpost(request):

  form = PostForm()

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    return redirect('index')


  context = {'form' : form}
  
  return render(request, "portfolio/post_form.html", context)


def readpost(request):
  
  return render(request, "portfolio/readpost.html")

@login_required(login_url='home')
def updatepost(request, slug):

  post = Post.objects.get(slug=slug)
  form = PostForm(instance=post)

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      form.save()
    return redirect('index')

  
  context = {'form' : form}

  
  return render(request, "portfolio/post_form.html", context)

@login_required(login_url='home')
def deletepost(request, slug):
  post = Post.objects.get(slug=slug)

  if request.method == 'POST':
    post.delete()
    return redirect ('posts')

  context = {'item' : post}


  
  return render(request, "portfolio/delete.html", context)


def sendEmail(request):
  if request.method == 'POST':
    template = render_to_string('porfolio/email_template.html',{
    'name':request.POST['name'],
    'email':request.POST['email'],
    'message':request.POST['message'],
  })
    email = EmailMessage(
    request.POST['subject'],
    template,
    settings.EMAIL_HOST_USER,['grari9187@gmail.com']
  )
    email.fail_silently=False
    email.send()


  return HttpResponse('Email was sent successfully')