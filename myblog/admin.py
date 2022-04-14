from django.contrib import admin
from . models import *
from django.utils.translation import gettext_lazy as _


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name','blog_date')
admin.site.register(Blog,BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved','post','created', 'email')

admin.site.register(Comment,CommentAdmin)