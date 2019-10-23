from django.shortcuts import render
from django.views.generic import TemplateView, View


class MyAccountInfo(TemplateView):
	template_name = '1208A-ASBD-DASHBOARD-MY-ACCOUNT-INFORMATION.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class MyAccountShipping(TemplateView):
	template_name = '1208B-ASBD-DASHBOARD-MY-ACCOUNT-SHIPPING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class PostAndSale(TemplateView):
	template_name = '2100-ASBD-POST-AND-SELL.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class ManagePosting(TemplateView):
	template_name = '2200-ASBD-MANAGE-POSTINGS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class SalesOrder(TemplateView):
	template_name = '2300-ASBD-SALES-ORDER.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class OrderHistory(TemplateView):
	template_name = '2400-ASBD-ORDER-HISTORY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})