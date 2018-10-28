from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.http import JsonResponse
from .models import Comment
from .models import CommentForm

# Create your views here.
def update_comment(request):
	referer = request.META.get('HTTP_REFERER', reverse('home'))
	commnet_form = CommentForm(request.POST, user=request.user)
	data = {}

	if comment_form.is_valid():
		# 检查通过，保存数据
		comment = Comment()