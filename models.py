from operator import mod
from pyexpat import model
from django.db import models

class Theme(models.Model):
    name = models.TextField(max_length=12)
class Post(models.Model):
    post = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    author = models.CharField(max_length=16)
    created = models.DateField(auto_now_add=True)
class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    author = models.CharField(max_length=16)
    created = models.DateField(auto_now_add=True)