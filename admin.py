
from django.contrib import admin
from .models import Post, Comment, Theme, LikeDis
class PostAdmin(admin.ModelAdmin):
    list_display =  ['title', 'text']
    list_filter = ['author', 'created']
    prepopulated_fields = {'slug': ('title',)}
class CommentAdmin(admin.ModelAdmin):
    list_display =  ['author', 'text']
    list_filter = ['author', 'created']
class ThemeAdmin(admin.ModelAdmin):
    list_display =  ['name']
    list_filter = ['name']
class LikeDisAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'vote']
    list_filter = ['user', 'post', 'vote']
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(LikeDis, LikeDisAdmin)