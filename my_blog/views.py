import datatime
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.core.cache import cache
from django.urls import reverse
from read_statistics.utils import get_seven_days_read_data, get_today_hot_data, get_yesterday_hot_data
from blog.models import blog

def get_7_days_hot_blogs():
	pass

def home():
	pass