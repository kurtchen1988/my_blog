from django import template # 这个要着重看一下tag的用法
from django.contrib.contenttypes.models import ContentType
from ..models import LikeCount, LikeRecord

register = template.Library()

@register.simple_tag
def get_like_count(obj):
	content_type = ContentType.object.get_for_model(obj)
	like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=obj.pk)
	return like_count.liked_num

@register.simple_tag(take_context=True)
def get_like_status(context, obj):
	