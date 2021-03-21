from django.contrib import admin
from .models import *
# Register your models here.


class PoemAdmin(admin.ModelAdmin):
    list_display = ('title','author','dynasty')
    search_fields = ['title','author__author']
    list_filter = ('dynasty','author',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author','dynasty')
    search_fields = ('author',)

class UsrAdmin(admin.ModelAdmin):
    list_display = ('username','password','nickname','icon')
    search_fields = ('username',)

admin.site.site_header = '古诗词学习网站后台管理系统'

admin.site.register(Poem,PoemAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Dynasty)
admin.site.register(Theme)
admin.site.register(Usr)

