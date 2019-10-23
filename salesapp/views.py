from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required



class PriceAndFee(TemplateView):
	template_name = '9031-PRICE-AND-FEE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class ManagePosting(TemplateView):
	template_name = '9032-MANAGE-POSTINGS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class SalesDataCustom(TemplateView):
	template_name = '9033-SALES-DATAS-NEW-CUSTOM-AND-USED-POSTING-FEE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class SalesOrder(TemplateView):
	template_name = '9034-SALES-ORDER-USED-BACKDROPS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class OrderHistory(TemplateView):
	template_name = '9035-ORDER-HISTORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


