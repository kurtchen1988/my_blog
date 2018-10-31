from django.urls import path
from . import views

urlpatterns = [
#地址为：localhost/blog/
	path('',views.blog_list, name='blog_list'), # 默认进入后显示博客列表
	path('<int:blog_pk>', views.blog_detail, name="blog_list"), # 显示博客列表的第n页，传入的是页码
	path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"), # 显示类型筛选过的博客列表，传入类型代码
	path('date/<int:year>/<int:month>',views.blogs_with_date, name="blogs_with_date"), # 显示某个日期的博客列表，传入年/月
]