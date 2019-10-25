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


class CompanyProf(TemplateView):
	template_name = '9061-COMPANY-PROFILE.html'
	def get(self, request, *args, **kwargs):
		try:
			profile = CompanyProfile.objects.latest('pk')
		except CompanyProfile.DoesNotExist:
			pass
		return render(request,self.template_name,locals())

	def post(self, request, *args, **kwargs):
		company_name = request.POST.get('company_name')
		address = request.POST.get('address')
		city = request.POST.get('city')
		state = request.POST.get('state')
		Zip = request.POST.get('zip')
		telephone = request.POST.get('telephone')
		email = request.POST.get('email')
		img = request.FILES.get('profile_pic')
		try:
			pro = CompanyProfile.objects.latest('pk')

			pro.company_name = company_name
			pro.address = address
			pro.city = city
			pro.state = state
			pro.Zip = Zip
			pro.telephone = telephone
			pro.email = email
			pro.profile_pic = img
			pro.save()
			return HttpResponseRedirect('/profile')

		except Exception as e:
			print(e)
			return HttpResponseRedirect('/profile')

