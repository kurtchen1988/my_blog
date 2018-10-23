import django.urls import auth
from . import views

urlpatterns = [
	path('',views.blog_list)
]