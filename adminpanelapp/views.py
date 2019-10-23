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


class AdminLogin(TemplateView):
	template_name = 'admin-login.html'
	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,{})

	def post(self,request,*args, **kwargs):
		admin_email = request.POST.get("email")
		admin_password = request.POST.get("password")
		remeber_password = request.POST.get("rember_me")

		try:
			user= User.objects.get(email=admin_email)
			userauth = authenticate(username=user.username, password=admin_password)
			if userauth:
					login(request, user,backend='django.contrib.auth.backends.ModelBackend')
					if request.user.is_authenticated:
						return HttpResponseRedirect('admin-home')

					else:
						return HttpResponseRedirect('admin-login')
			else:
				messages.error(request,'Incorrect password given.')
				return HttpResponseRedirect('admin-login')

		except Exception as e:
			print(e)
			messages.error(request,'Incorrect email address given.')
			return HttpResponseRedirect('admin-login')



class AdminLogout(View):
	def get(self,request,*args, **kwargs):
		logout(request)
		return HttpResponseRedirect('admin-login')


class AdminHome(TemplateView):
	template_name = '9000-SUMMARY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class SuperAdmin(TemplateView):
	template_name = '9001-SUPER-ADMIN.html'
	def get(self, request, *args, **kwargs):
		users = User.objects.filter(is_staff=True).exclude(is_superuser=True)
		return render(request,self.template_name,locals())



class EditAdmin(TemplateView):
	template_name = 'edit-admin.html'
	def get(self, request, *args, **kwargs):
		user_id = kwargs.get('user_id')
		user = User.objects.get(id=user_id)
		user_groups = user.groups.all()
		current_id = 0
		if user_groups:
			current_id = user_groups[0].id
		groups = Group.objects.all()
		model_items = ContentType.objects.exclude(app_label__in=["auth","contenttypes","sessions","social_django","admin"])
		selected_permissions = set(Permission.objects.filter(user=user_id).values_list('content_type__model',flat=True).distinct())
		model_list = map(lambda model_item: {"id":model_item.id,"name":model_item.name,"slug":(model_item.name).replace(" ","")}, model_items) 

		return render(request,self.template_name,locals())


	def post(self,request,*args, **kwargs):
		user_id = kwargs.get('user_id')
		name = request.POST.get('name')
		old_pass = request.POST.get('old_pass')
		new_pass = request.POST.get('password')
		role = request.POST.get('role')
		status = request.POST.get('status')
		email = request.POST.get('email')
		selected_models = request.POST.getlist('models[]')
		email = email.lower()
		
		
		try:
			user = User.objects.get(id=user_id)
			if old_pass=="" and new_pass=="":
				user.first_name=name
				user.username=email
				user.email=email
				user.is_staff = True
				if status=="A":
					user.is_active = True
				else:
					user.is_active = False
				# user.set_password(password)
				user.save()

				group = Group.objects.get(id=role) 
				group.user_set.add(user)
				group.save()
				permission_list = Permission.objects.filter(content_type_id__in = selected_models)
				user.user_permissions.set(permission_list)
				user.save()

				messages.success(request, 'Staff entry done successfully.')
				return HttpResponseRedirect('/admin/super_admin')
			else:
				userauth = authenticate(username=user.username, password=old_pass)
				if userauth:
					user.first_name=name 
					user.username=email
					user.email=email
					user.is_staff = True
				if status=="A":
					user.is_active = True
				else:
					user.is_active = False
				user.set_password(new_pass)
				user.save()

				group = Group.objects.get(id=role) 
				group.user_set.add(user)
				group.save()
				permission_list = Permission.objects.filter(content_type_id__in = selected_models)
				user.user_permissions.set(permission_list)
				user.save()

				messages.success(request, 'Staff entry done successfully.')
				return HttpResponseRedirect('/admin/super_admin')



		except Exception as e:
			print(str(e))
			return HttpResponseRedirect('/admin/edit_admin/'+str(user_id))




class DeleteAdmin(View):
	def get(self, request, *args, **kwargs):
		user_id = kwargs.get('user_id')
		try:
			user = User.objects.get(id=user_id)
			print(user)
			user.delete()
			return HttpResponseRedirect('/admin/super_admin')
			
		except Exception as e:
			print(str(e))
			return HttpResponseRedirect('super_admin')


class AddStaff(TemplateView):
	template_name = '9002-ADD-STAFF.html'
	def get(self, request, *args, **kwargs):
		group_list = Group.objects.all()
		model_list = ContentType.objects.exclude(app_label__in=["auth","contenttypes","sessions","social_django","admin"])
		return render(request,self.template_name,locals())
		


	def post(self,request,*args, **kwargs):
		print(request.POST)
		name = request.POST.get('name')
		password = request.POST.get('password')
		role = request.POST.get('role')
		status = request.POST.get('status')
		email = request.POST.get('email')
		selected_models = request.POST.getlist('models[]')
		email = email.lower()
		try:
			User.objects.get(email=email)
			messages.error(request, 'User already exists with given email.')
		except User.DoesNotExist:
			user = User.objects.create_user(
				email=email,
				username=email,
				first_name=name
				)
			user.is_staff = True
			if status=="A":
				user.is_active = True
			else:
				user.is_active = False
			user.set_password(password)
			user.save()

			group = Group.objects.get(id=role) 
			group.user_set.add(user)
			group.save()
			permission_list = Permission.objects.filter(content_type_id__in = selected_models)
			user.user_permissions.set(permission_list)
			user.save()
			messages.success(request, 'Staff entry done successfully.')
		return HttpResponseRedirect('add_staff')





class Users(TemplateView):
	template_name = '9003-USERS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})




class GeneralConfiguration(TemplateView):
	template_name = '9051-GENERAL-CONFIG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class CompanyProfile(TemplateView):
	template_name = '9061-COMPANY-PROFILE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class Paypal(TemplateView):
	template_name = '9081-PAYPAL.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})






