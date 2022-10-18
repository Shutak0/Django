
from django.contrib import admin
from .models import Post, Comment, Theme
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
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Theme, ThemeAdmin)