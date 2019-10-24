from django.urls import path
from .views import *

urlpatterns = [
	path('', login_required(GeneralConfiguration.as_view()), name="admin_config"),


]