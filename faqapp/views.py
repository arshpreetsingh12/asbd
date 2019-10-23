from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class FaqCategory(TemplateView,LoginRequiredMixin):
	template_name = '9021-FAQ-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		categories = FAQCategory.objects.all()
		return render(request,self.template_name,locals())

	# Delete Faq category 
	def post(self,request):
		cat_id = request.POST.get('cat_id')
		FAQCategory.objects.get(pk = cat_id).delete()
		messages.success(request,'Successfully deleted')
		response = {}
		return HttpResponse(json.dumps(response), content_type="application/json")



class AddFaqCategory(TemplateView):
	template_name = '9022-ADD-FAQ-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self, request, *args, **kwargs):
		status = request.POST.get("status")
		order = request.POST.get("order")
		category = request.POST.get("category")
		if status and category and order:
			cat = FAQCategory(category_name = category,sort_order = order)
			if status == 'active':
				cat.status = True
			cat.save()
			messages.success(request,'FAQ Category Successfully Added')
		else:
			messages.error(request,'Something Went Wrong')
		return HttpResponseRedirect('/faqapp/faq_category')



class EditFAQCategory(TemplateView):
	def get(self,request, cat_id):
		cat = FAQCategory.objects.get(pk = cat_id)
		return render(request,'Edit-faq-category.html',locals())


	def post(self,request,cat_id):
		cat_id = cat_id
		status =  request.POST.get('status')
		order =  request.POST.get('order')
		name =  request.POST.get('category')
		try:
			if cat_id:
				category = FAQCategory.objects.get(pk = cat_id)
				if name:
					category.category_name = name
				if order:
					category.sort_order = order
				if status == 'active':
					category.status = True
				else:
					category.status = False
				category.save()
				messages.success(request,'FAQ Category Successfully Added')
			else:
				messages.error(request,'Something Went Wrong')
		except Exception as e:
			messages.error(request,'Something Went Wrong')
		return HttpResponseRedirect('/faqapp/faq_category')



class Faq(TemplateView):
	template_name = '9023-FAQ.html'
	def get(self, request, *args, **kwargs):
		faqs = FAQ.objects.all()
		return render(request,self.template_name,locals())


	# delete faq
	def post(self,request):
		faq_id = request.POST.get('faq_id')
		FAQ.objects.get(pk = faq_id).delete()
		response = {}
		return HttpResponse(json.dumps(response), content_type="application/json")



class AddFaq(TemplateView):
	template_name = '9024-ADD-FAQ.html'
	def get(self, request, *args, **kwargs):
		category = FAQCategory.objects.all()
		return render(request,self.template_name,locals())


	def post(self, request, *args, **kwargs):
		category_id = request.POST.get('category')
		question = request.POST.get('question')
		order = request.POST.get('order')
		status = request.POST.get('status')
		answer = request.POST.get('answer')

		if category_id and question and answer:
			faq = FAQ(category_id = category_id, question = question, answer = answer)
			if status == 'active':
				faq.status = True
			if order:
				faq.sort_order = order
			faq.save()
		return HttpResponseRedirect('/faqapp/faq')


class EditFaq(View):
	def get(self,request, faq_id):
		category = FAQCategory.objects.all()
		faq = FAQ.objects.get(pk = faq_id)
		return render(request,'edit-faq.html',locals())

	def post(self, request, faq_id):
		faq_id = faq_id
		category_id = request.POST.get('category')
		question = request.POST.get('question')
		order = request.POST.get('order')
		status = request.POST.get('status')
		answer = request.POST.get('answer')

		try:
			if faq_id:
				faq = FAQ.objects.get(pk = faq_id)
				if category_id:
					faq.category_id = category_id
				if order:
					faq.sort_order = order
				if status == 'active':
					faq.status = True
				if question:
					faq.question = question
				if answer:
					faq.answer = answer
				else:
					faq.status = False
				faq.save()
				messages.success(request,'FAQ Category Successfully Added')
			else:
				messages.error(request,'Something Went Wrong')
		except Exception as e:
			messages.error(request,'Something Went Wrong')
		return HttpResponseRedirect('/faqapp/faq')

