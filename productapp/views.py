from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required


class ProductList(TemplateView):
	template_name = '9041-PRODUCT-LIST.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddProduct(TemplateView):
	template_name = '9042-ADD-PRODUCT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})




class ShippingList(TemplateView):
	template_name = '9043-SHIPPING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddShipping(TemplateView):
	template_name = '9044-ADD-SHIPPING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

