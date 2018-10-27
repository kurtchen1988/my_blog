import django.urls import auth
from . import views

urlpatterns = [
#地址为：localhost/blog/
	path('',views.blog_list, name='blog_list'), # 默认进入后显示博客列表
	path('<int:blog_pk>', views.blog_detail, name="blog_list"),
]