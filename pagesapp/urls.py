from django.urls import path
from .views import *

urlpatterns = [
	path('manage_page', login_required(ManagePage.as_view()), name="manage_page"),
	path('add_page', login_required(AddPage.as_view()), name="add_page"),
	path('edit_page/<page_id>', login_required(EditPage.as_view()), name="edit_page"),
	path('delete_page', login_required(DeletePage.as_view()), name="delete_page"),
	path('single_page_status', login_required(PageStatus.as_view()), name="single_page_status"),
	path('selected-pages-status', login_required(SelectedPageStatus.as_view()), name="selected-pages-status"),

]