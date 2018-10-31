from django.contrib import admin
from . models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	'''注册评论模块'''
	list_display = ('id','content_object', 'text','comment_time','user','root','parent')