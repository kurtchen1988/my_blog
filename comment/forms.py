from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from .models import Comment
# https://docs.djangoproject.com/en/2.1/topics/forms/
# 上面的文章要好好读，写了所有关于表单的基本介绍
class CommentForm(forms.Form):
	content_type = forms.CharField(widget=forms.HiddenInput)
	# 内容类型，是字符串类型，在表单中为隐藏项
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	# 项目类型，是整数型，在表单中为隐藏项
	text = forms.CharField(widget=CKEditorWidget(config_name = 'comment_ckeditor'), error_messages={'required':'评论内容不能为空'})
	# 回复内容，是字符串类型，在表单中是CKEditorWidget，错误信息为需要填入信息
	reply_comment_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'reply_comment_id'}))
	# 回复id，是整数型，在表单中为隐藏类型
	def __init__(self, *args, **kwargs):
		if 'user' in kwargs:
			self.user = kwargs.pop('user')
		super(CommentForm, self).__init__(*args, **kwargs)

	def clean(self):
		# 判断用户是否登录，如果没登陆报一个验证错
		if self.user.is_authenticated:
			self.cleaned_data['user'] = self.user # https://docs.djangoproject.com/en/2.1/ref/forms/validation/
			# 这里的cleaned_data是django的验证步骤

		else:
			raise forms.ValidationError('用户尚未登录')

		# 评论对象验证
		content_type = self.cleaned_data['content_type']
		object_id = self.cleaned_data['object_id']

		try:
			model_class = ContentType.objects.get(model=content_type).model_class()
			model_obj = model_class.objects.get(pk=object_id)
			self.cleaned_data['content_object'] = model_obj
		except ObjectDoesNotExist:
			raise forms.ValidationError('评论对象不存在')

		return self.cleaned_data

	def clean_reply_comment_id(self):
		'''清除回复的id，当回复id为0意思是它为文章的第一个留言，小于0是错的，当它回复的id存在就拿到它的信息，否则报错'''
		reply_comment_id = self.cleaned_data['reply_comment_id']
		if reply_comment_id < 0:
			raise forms.ValidationError('回复出错')
		elif reply_comment_id == 0:
			self.cleaned_data['parent'] = None
		elif Comment.objects.filter(pk=reply_comment_id).exists():
			self.cleaned_data['parent'] = Comment.objects.get(pk=reply_comment_id)
		else:
			raise forms.ValidationError('回复出错')
		return reply_comment_id