from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm

register = template.Library()

@register.simple_tag
def get_comment_count(obj):
	'''注册自定义标签，返回评论个数'''
	content_type = ContentType.objects.get_for_model(obj)
	return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()

@register.simple_tag
def get_comment_form(obj):
	'''返回表单，并注册自定义标签'''
	content_type = ContentType.objects.get_for_model(obj)
	form = CommentForm(initial={'content_type':content_type.model,'object_id':obj.pk,'reply_comment_id':0})
	return form

@register.simple_tag
def get_comment_list(obj):
	'''返回评论的结果集，并以评论时间倒序排列'''
	content_type = ContentType.objects.get_for_model(obj)
	comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
	return comments.order_by('-comment_time')