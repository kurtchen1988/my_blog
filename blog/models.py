from django.db import models
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/2.1/ref/contrib/auth/
from django.contrib.contenttypes.fields import GenericRelation # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
# Create your models here.
class BlogType(models.Model):
	'''博客类型：类型名称'''
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.auth.email

class Blog(models.Model, ReadNumExpandMethod):
	'''博客内容：标题，类型（外键，与博客类型相连），博客内容，作者，？（统计里的ReadDetail），创建时间，最后修改时间'''
	title = models.CharField(max_length=50)
	blog_type = models.ForeignKey(BlogType, on_delete = models.CASCADE)
	content = RichTextUploadingField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	read_details = GenericRelation(ReadDetail)
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now_add=True)

	def get_url(self):
		'''得到url，reverse到blog_detail,传入参数为带有主键的博客'''
		return reverse('blog_detail', kwargs={'blog_pk':self.pk})

	def get_email(self):
		'''返回email'''
		return self.author.email

	def __str__(self, arg):
		'''重写显示内容，展示博客标题'''
		return "<Blog: %s>"%self.title
		
	class Meta:
		'''Meta类，复写排序顺序'''
		ordering = ['-created_time']