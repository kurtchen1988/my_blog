from django.contrib import admin # https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
from .models import BlogType, Blog

# Register your models here.
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
	'''注册博客类型'''
	list_display = ('id', 'type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	'''注册博客内容'''
	list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')