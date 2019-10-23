from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required



class FaqCategory(TemplateView):
	template_name = '9021-FAQ-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddFaqCategory(TemplateView):
	template_name = '9022-ADD-FAQ-CATEGORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class Faq(TemplateView):
	template_name = '9023-FAQ.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddFaq(TemplateView):
	template_name = '9024-ADD-FAQ.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})
