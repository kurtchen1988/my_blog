from django.db import models
from django.contrib.auth.models import User # https://docs.djangoproject.com/en/2.1/ref/contrib/auth/
from django.contrib.contenttypes.fields import GenericRelation # https://docs.djangoproject.com/en/2.1/ref/contrib/contenttypes/
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
# Create your models here.
class BlogType(models.Model):
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.auth.email

class ClassName(models.Model, ReadNumExpandMethod):
	title = models.CharField(max_length=50)
	blog_type = models.ForeignKey(BlogType, on_delete = models.CASCADE)
	content = RichTextUploadingField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	read_details = GenericRelation(ReadDetail)
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now_add=True)

	def get_url(self):
		return reverse('blog_detail', kwargs={'blog_pk':self.pk})

	def get_email(self):
		return self.author.email

	def __str__(self, arg):
		return "<Blog: %s>"%self.title
		
	class Meta:
		ordering = ['-created_time']