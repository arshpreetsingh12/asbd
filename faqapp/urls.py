
from django.urls import path
from .views import *

urlpatterns = [
	path('faq_category', login_required(FaqCategory.as_view()), name="faq_category"),
	path('add_faq_category', login_required(AddFaqCategory.as_view()), name="add_faq_category"),
	path('faq', login_required(Faq.as_view()), name="faq"),
	path('add_faq', login_required(AddFaq.as_view()), name="add_faq"),


]