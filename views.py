from django.shortcuts import render
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