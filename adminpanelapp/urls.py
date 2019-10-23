
from django.urls import path
from .views import *

urlpatterns = [
	path('admin-login', AdminLogin.as_view(), name="admin-login"),
	path('admin-logout', AdminLogout.as_view(), name="admin-logout"),
	path('admin-home', login_required(AdminHome.as_view()), name="admin-home"),
	path('super_admin', login_required(SuperAdmin.as_view()), name="super_admin"),
	path('delete_admin/<user_id>', login_required(DeleteAdmin.as_view()), name="delete_admin"),
	path('edit_admin/<user_id>', login_required(EditAdmin.as_view()), name="edit_admin"),
	path('add_staff', login_required(AddStaff.as_view()), name="add_staff"),
	path('users', login_required(Users.as_view()), name="users"),
	
	path('general_configuration', login_required(GeneralConfiguration.as_view()), name="general_configuration"),
	path('company_profile', login_required(CompanyProfile.as_view()), name="company_profile"),
	
	path('paypal', login_required(Paypal.as_view()), name="paypal"),


]

