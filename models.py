from ast import arg
from operator import mod
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
class Theme(models.Model):
    name = models.TextField(max_length=12)
class Post(models.Model):
    post = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=16)
    created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, db_index=True)
    def get_absolutely_url(self):
        return reverse('forum:post', args=[self.id, self.slug])
    def get_comment(post):
        return Comment.objects.filter(product=post)
class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    author = models.CharField(max_length=16)
    created = models.DateField(auto_now_add=True)

