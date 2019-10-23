from django.urls import path
from .views import *

urlpatterns = [
	path('new_and_used_images', login_required(NewAndUsedImages.as_view()), name="new_and_used_images"),
	path('add_new_images', login_required(AddNewImages.as_view()), name="add_new_images"),

]