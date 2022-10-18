from itertools import product
from tracemalloc import get_object_traceback
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
def index(request):
    posts = Post.objects.all()
    return render(request, 'forum/index.html', {'posts':posts})
def faq(request):
    return render(request, 'forum/faq.html', {})
def latest(request):
    return render(request, 'forum/latest.html', {})
def popular(request):
    return render(request, 'forum/popular.html', {})
def comments(request):
    return render(request, 'forum/comments.html', {})
def send(request):
    return render(request, 'forum/send.html')
def ckartinka(request):
    return render(request, 'img/weee.png')
def post(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'forum/comments.html', {'post': post})