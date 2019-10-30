from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
import json


class ProductList(TemplateView):
	template_name = '9041-PRODUCT-LIST.html'
	def get(self, request, *args, **kwargs):
		product = Product.objects.all()
		return render(request,self.template_name,locals())



class AddProduct(TemplateView):
	template_name = '9042-ADD-PRODUCT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self, request, *args, **kwargs):
		total_boxes = request.POST['product_box']

		if request.POST:
			j = 0
			
			for i in range(j,int(total_boxes)+1):
				product_name = ''
				width = ''
				height = ''
				weight = ''
				price = ''
				process_time = ''
				backdrop_type = ''
				flag=0
				try:

					if 'product_name'+str(i) in request.POST:
						product_name = request.POST['product_name'+str(i)]
						flag = 1
		

					if 'width'+str(i) in request.POST:
						width = request.POST['width'+str(i)]
						flag = 1

					if 'height'+str(i) in request.POST:
						height = request.POST['height'+str(i)]
						flag = 1

					if 'weight'+str(i) in request.POST:
						weight = request.POST['weight'+str(i)]
						flag = 1

					if 'price'+str(i) in request.POST:
						price = request.POST['price'+str(i)]
						flag = 1

					if 'process_time'+str(i) in request.POST:
						process_time = request.POST['process_time'+str(i)]
						flag = 1

					if 'backdrop_type'+str(i) in request.POST:
						backdrop_type = request.POST['backdrop_type'+str(i)]
						flag = 1

					if flag == 1:
						Product.objects.create(product_name=product_name, width=width, height=height, weight=weight, price=price, process_time=process_time, backdrop_type=backdrop_type)
				except Exception as e:
					print(e)
		return HttpResponseRedirect('add_product')



class EditProduct(TemplateView):
	template_name = 'edit-product.html'
	def get(self,request, product_id):
		product = Product.objects.get(pk=product_id)
		return render(request,self.template_name,locals())

	def post(self, request, product_id):
		product_id = product_id
		product_name = request.POST.get('product_name')
		width = request.POST.get('width')
		height = request.POST.get('height')
		weight = request.POST.get('weight')
		price = request.POST.get('price')
		process_time  = request.POST.get('process_time')
		backdrop_type = request.POST.get('exampleRadios')
		Product.objects.filter(pk=product_id).update(product_name=product_name, width=width, height=height, weight=weight, price=price, process_time=process_time, backdrop_type=backdrop_type)
		return HttpResponseRedirect('/productapp/product_list')




class ShippingList(TemplateView):
	template_name = '9043-SHIPPING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddShipping(TemplateView):
	template_name = '9044-ADD-SHIPPING.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

