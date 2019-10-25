from django.urls import path
from .views import *

urlpatterns = [
		path('', login_required(CompanyProf.as_view()), name="company_profile"),


]