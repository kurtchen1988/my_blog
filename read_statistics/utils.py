import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail

def read_statistics_once_read(request, obj):
	ct = ContentType.objects.get_for_model(obj)
	key = "%s_%s_read"%(ct.model, obj.pk)

	if not request.COOKIE.get(key):
		# 总阅读数 +1
		readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
		readnum.read_num += 1
		readnum.save()