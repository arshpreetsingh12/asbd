from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from random import *
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string



class Homepage(TemplateView):
	template_name = '1000-ASBD-HOME-PAGE.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})
	


class New(TemplateView):
	template_name = '1100-ASBD-NEW.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Custom(TemplateView):
	template_name = '1120-ASBD-CUSTOM.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Used(TemplateView):
	template_name = '1130-ASBD-USED.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class MyCartInvitation(TemplateView):
	template_name = '1140-ASBD-MY CART-invitation.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class MyCartTag(TemplateView):
	template_name = '1140-ASBD-MY CART-tag-2.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class MyCart(TemplateView):
	template_name = '1140-ASBD-MY-CART.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class MyOrder(TemplateView):
	template_name = '1150-ASBD-MY-ORDER.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class MyOrderTag(TemplateView):
	template_name = '1150-ASBD-MY-ORDER-Tag-2.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class WishDropGreeting(TemplateView):
	template_name = '1180-ASBD-WISHDROPS-GREETING-FORM.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class AboutUs(TemplateView):
	template_name = '1201-NAV-BAR-ABOUT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})



class WhyUs(TemplateView):
	template_name = '1202-NAV-BAR-WHY US.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Faq(TemplateView):
	template_name = '1203-NAV-BAR-FAQ.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class ContactUs(TemplateView):
	template_name = '1204-NAV-BAR-CONTACT.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Terms(TemplateView):
	template_name = '1205-NAV-BAR-TERMS.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Privacy(TemplateView):
	template_name = '1206-NAV-BAR-PRIVACY.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

class Blog(TemplateView):
	template_name = '1207-NAV-BAR-BLOG.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class Registration(TemplateView):
	template_name = '1300-NAV-BAR-REGISTRATION.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})

	def post(self, request, *args, **kwargs):
		first_name = request.POST.get('f_name')
		last_name = request.POST.get('l_name')
		parent_email = request.POST.get('parent_email')
		parent_password = request.POST.get('parent_password')
		country = request.POST.get('parent_country')
		state = request.POST.get('state')
		terms = request.POST.get('terms')

		try:
			user=User.objects.get(email=parent_email)
			messages.info(request,"User already Exist.")
			return HttpResponseRedirect("registration")

		except User.DoesNotExist:
			parent=User.objects.create_user(
				username=parent_email,
				email=parent_email,
				password=parent_password
				)
			parent.first_name=first_name
			parent.last_name=last_name
			
			parent.is_active=True
			parent.save()
			parent.set_password('password')
			
			profile=Profile(user=parent,country=country,state=state,terms_condition=terms)
			messages.success(request, 'Successfully Register.')
			profile.save()
			# login(request, parent)
			login(request, parent,backend='django.contrib.auth.backends.ModelBackend')
			return HttpResponseRedirect("used")

class Login(View):
	def post(self, request, *args, **kwargs):
			email = request.POST.get('email')
			password = request.POST.get('password')
			print(">>>>password",password)
			try:
				user= User.objects.get(email=email)
				userauth = authenticate(username=user.username, password=password)
				
				if userauth:
					# login(request, user)
					login(request, user,backend='django.contrib.auth.backends.ModelBackend')
					if request.user.is_authenticated:
						return HttpResponseRedirect('used')
					else:
						return HttpResponseRedirect('registration')
				else:
					
					messages.error(request,'Incorrect password given.')
					return HttpResponseRedirect('registration')

			except Exception as e:
				print(e)
				messages.error(request,'Incorrect email address given.')
				return HttpResponseRedirect('registration')


class LogoutView(View):
	def get(self,request,*args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')


class ForgetPassword(TemplateView):
	template_name = '1310-NAV-BAR-FORGET PASSWORD-TAG-1.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class ResetPassword(TemplateView):
	template_name = '1320-NAV-BAR-RESET PASSWORD.html'
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


