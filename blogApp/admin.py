from django.contrib import admin
from . models import *

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ['title','intro','file','body']
    
class AdminComment(admin.ModelAdmin):
    list_display = ['post','email','comment_text']

admin.site.register(Post,AdminPost)
admin.site.register(Comment,AdminComment)
