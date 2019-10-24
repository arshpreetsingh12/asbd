from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission 
from django.contrib.contenttypes.models import ContentType 
from django.apps import apps
from .models import *
import json
from django.http import HttpResponse





class GeneralConfiguration(TemplateView):
	template_name = '9051-GENERAL-CONFIG.html'
	def get(self, request, *args, **kwargs):
		try:
			config = Config.objects.latest('pk')
		except Config.DoesNotExist:
			pass
		return render(request,self.template_name,locals())

	def post(self,request):
		maintaince_mode = request.POST.get('maintaince_mode')
		try:
			config = Config.objects.latest('pk')
			for obj in request.POST:
				if obj != 'csrfmiddlewaretoken' or obj != 'maintaince_mode':
					setattr(config , obj, request.POST[obj])
			if maintaince_mode == 'yes':
				config.maintaince_mode = True
			else:
				config.maintaince_mode = False
			config.save()
		except Config.DoesNotExist:
			config = Config()
			for obj in request.POST:
				if obj != 'csrfmiddlewaretoken' or obj != 'maintaince_mode':
					setattr(config , obj, request.POST[obj])
			if maintaince_mode == 'yes':
				config.maintaince_mode = True
			else:
				config.maintaince_mode = False
			config.save()
		return HttpResponseRedirect('/config')