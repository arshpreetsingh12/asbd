from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
import json


class ManagePage(TemplateView):
	template_name = '9011-MANAGE-CONTENT.html'
	def get(self, request, *args, **kwargs):
		pages=Page.objects.all().order_by('-id')
		return render(request,self.template_name,locals())


class AddPage(TemplateView):
	template_name = '9012-ADD-PAGES.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self,request, *args , **kwargs):
		title = request.POST.get("page_title")
		content = request.POST.get("page_content")
		url = request.POST.get("page_url")
		page_obj = Page(
			title=title,
			content=content,
			url=url
			)

		page_obj.save()
		return HttpResponseRedirect('/pagesapp/manage_page')


class EditPage(TemplateView):
	template_name = '9013-EDIT-PAGE.html'
	def get(self, request, *args, **kwargs):
		page_id = kwargs.get('page_id')
		try:
			page=Page.objects.get(id=page_id)
		except Exception as e:
			raise e
		return render(request,self.template_name,locals())

	def post(self, request, *args, **kwargs):
		page_id = kwargs.get('page_id')
		title = request.POST.get('edit_title')
		content = request.POST.get('edit_content')
		url = request.POST.get('edit_url')
		try:
			updated_page = Page.objects.get(id=page_id)
			updated_page.title = title
			updated_page.content = content 
			updated_page.url = url
			updated_page.save()
			return HttpResponseRedirect('/pagesapp/manage_page')

		except Exception as e:
			raise e
			return HttpResponseRedirect('/pagesapp/manage_page')


class DeletePage(View):
	def get(self, request, *args, **kwargs):
		page_id = kwargs.get('page_id')
		try:
			page = Page.objects.get(id=page_id)
			page.delete()
			return HttpResponseRedirect('/pagesapp/manage_page')
			
		except Exception as e:
			print(str(e))
			return HttpResponseRedirect('/pagesapp/manage_page')



#change single page status 

class PageStatus(View):
	def get(self, request, *args, **kwargs):
		page_id = kwargs.get('page_id')
		try:
			page = Page.objects.get(id=page_id)
			if page.status:
				page.status=False
			elif page.status==False:
				page.status=True
			page.save()
			return HttpResponseRedirect('/pagesapp/manage_page')
			
		except Exception as e:
			print(str(e))
			
			return HttpResponseRedirect('/pagesapp/manage_page')

# change selected page status 

class SelectedPageStatus(View):
	def get(self, request, *args, **kwargs):
		page_id = request.GET.getlist('page_id[]')
		status=request.GET.get('status')
		response={}
		try:
			if status=='true':
				Page.objects.filter(id__in=page_id).update(status=True)
			else:
				Page.objects.filter(id__in=page_id).update(status=False)
			response['status']=True
		except Exception as e:
			raise e
			response['status']=False
		return HttpResponse(json.dumps(response), content_type="application/json")


class GetPages(View):
	template_name='dynamic_page.html'
	def get(self, request, *args, **kwargs):
		try:
			url=kwargs.get('page')
			page_html=Page.objects.get(url=url)
		except Exception as e:
			raise e
		return render(request,self.template_name,locals())