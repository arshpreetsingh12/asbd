from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required




class TypesOfUse(TemplateView):
	template_name = '9091-TYPE-OF-USE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Keywords(TemplateView):
	template_name = '9092-KEYWORDS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class CouponList(TemplateView):
	template_name = '9098-COUPON.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class AddCoupon(TemplateView):
	template_name = '9099-ADD-COUPON.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})
