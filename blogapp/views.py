from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect,HttpResponse
import json


class BlogCategoryView(TemplateView):
	template_name = '9071-BLOG-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		blog_cats = BlogCategory.objects.all()
		return render(request,'9071-BLOG-CATEGORY.html',locals())

	# delete category 
	def post(self,request):
		cat_id = request.POST.get('cat_id')
		BlogCategory.objects.get(pk = cat_id).delete()
		response = {}
		return HttpResponse(json.dumps(response), content_type="application/json")



class AddBlogCategory(TemplateView):
	template_name = '9072-ADD-BLOG-CATEGORY.html'
	def get(self, request):
		return render(request,self.template_name,{})

	def post(self, request):
		status = request.POST.get('status')
		sort= request.POST.get('order')
		category = request.POST.get('category')

		if status and category and sort:
			cat = BlogCategory(category_name=category,sort_order=sort)
			if status == 'active':
				cat.status = True
			cat.save()
			messages.success(request,'Blog Category Category Successfully Added')

		else:
			messages.error(request,'Something Went Wrong')
		return HttpResponseRedirect('/blogapp/blog_category')



class EditBlogCategory(View):
	def get(self, request,cat_id):
		cat = BlogCategory.objects.get(pk = cat_id)
		return render(request,'edit-blog-category.html',locals())

	def post(self,request,cat_id):
		cat_id = cat_id
		status =  request.POST.get('status')
		order =  request.POST.get('order')
		name =  request.POST.get('category')
		try:
			if cat_id:
				category = BlogCategory.objects.get(pk = cat_id)
				if name:
					category.category_name = name
				if order:
					category.sort_order = order
				if status == 'active':
					category.status = True
				else:
					category.status = False
				category.save()
				messages.success(request,'Blog Category Successfully Added')
			else:
				messages.error(request,'Something Went Wrong')
		except Exception as e:
			messages.error(request,'Something Went Wrong')
		return HttpResponseRedirect('/blogapp/blog_category')




class BlogList(TemplateView):
	template_name = '9073-BLOG-LIST.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddBlog(TemplateView):
	template_name = '9074-ADD-BLOG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})