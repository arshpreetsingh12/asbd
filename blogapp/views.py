from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required


class BlogCategory(TemplateView):
	template_name = '9071-BLOG-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddBlogCategory(TemplateView):
	template_name = '9072-ADD-BLOG-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class BlogList(TemplateView):
	template_name = '9073-BLOG-LIST.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddBlog(TemplateView):
	template_name = '9074-ADD-BLOG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})