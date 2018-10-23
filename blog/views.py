from django.shortcuts import get_object_or_404, render  # https://docs.djangoproject.com/en/2.1/_modules/django/shortcuts/
from django.core.paginator import Paginator # https://docs.djangoproject.com/en/2.1/topics/pagination/
from django.conf import settings # https://docs.djangoproject.com/en/2.1/ref/settings/
from django.db.models import Count # https://docs.djangoproject.com/en/2.1/topics/db/aggregation/
from django.contrib.contenttypes.models import ContentType # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/

from .models import Blog, BlogType
from read_statistics.utils import read_statistics_once_read

# Create your views here.
def get_blog_list_common_data(request, blogs_all_list):
	paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
	page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
	page_of_blogs = paginator.get_page(page_num)
	current_page_num = page_of_blogs.number # 获取当前页面
	# 获取当前页码前后2页的页码范围
	page_range = list(range(max(current_page_num - 2, 1), current_page_num)) +\
	list(range(current_page_num, min(current_page_num+2, paginator.num_pages)+1))
	