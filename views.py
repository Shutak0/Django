from itertools import product
from tracemalloc import get_object_traceback
from urllib import request
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
from .models import Comment
def index(request):
    posts = Post.objects.all()
    return render(request, 'forum/index.html', {'posts':posts})
def faq(request):
    return render(request, 'forum/faq.html', {})
def latest(request):
    return render(request, 'forum/latest.html', {})
def popular(request):
    return render(request, 'forum/popular.html', {})
def postik(request):
    return render(request, 'forum/postik.html', {})
def send(request):
    return render(request, 'forum/send.html')
def ckartinka(request):
    return render(request, 'img/weee.png')
def post(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    if request.method == 'POST':
        client_text = request.POST.get('text', False)
        comment = Comment(text=client_text, author='ádmín', post=post)
        comment.save()
    return render(request, 'forum/postik.html', {'post': post})