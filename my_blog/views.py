import datatime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from blog.models import blog

def get_7_days_hot_blogs():
	today = timezone.now().data()
	date = today - datatime.timedelta(days = 7)
	blogs = Blog.objects.filter(read_details__date__lt=today)

def home():
	pass