from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
import json
from django.shortcuts import  get_object_or_404


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
		image = request.FILES.get('img')
		page_obj = Page(
			title=title,
			content=content,
			url=url,
			image=image 
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
		image = request.FILES.get('edit_img')
		try:
			updated_page = Page.objects.get(id=page_id)
			updated_page.title = title
			updated_page.content = content 
			updated_page.url = url
			updated_page.image = image

			updated_page.save()
			return HttpResponseRedirect('/pagesapp/manage_page')

		except Exception as e:
			raise e
			return HttpResponseRedirect('/pagesapp/manage_page')




class DeletePage(View):
	def get(self,request):
			page_id = request.GET.get('page_id')
			response={}
			try:
				Page.objects.get(id=int(page_id)).delete()
				response['status']=True
			except Exception as e:
				raise e
				response['status']=False
			return HttpResponse(json.dumps(response), content_type="application/json")



#change single page status 
class PageStatus(View):
	def get(self,request):
		page_id = request.GET.get('page_id')
		response={}
		try:
			page_obj=Page.objects.get(id=int(page_id))
			if page_obj.status:
				page_obj.status=False
			elif page_obj.status==False:
				page_obj.status=True
			page_obj.save()
			response['status']=True
		except Exception as e:
			raise e
			response['status']=False
		return HttpResponse(json.dumps(response), content_type="application/json")



# change selected page status 

class SelectedPageStatus(View):
	def post(self,request):
		selected = request.POST.getlist('selected_pages[]')
		status=request.POST.get('status')
		response={}
		try:
			if status=='true':
				Page.objects.filter(id__in=selected).update(status=True)
			else:
				Page.objects.filter(id__in=selected).update(status=False)
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
			page_html=get_object_or_404(Page, url=url)
		except Exception as e:
			raise e
		return render(request,self.template_name,locals())