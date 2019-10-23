from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required


class NewAndUsedImages(TemplateView):
	template_name = '9093-MANAGE-NEW-AND-USE-IMAGES.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class AddNewImages(TemplateView):
	template_name = '9094-ADD-NEW-IMAGES.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


