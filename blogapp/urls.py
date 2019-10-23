
from django.urls import path
from .views import *

urlpatterns = [
	path('blog_category', login_required(BlogCategoryView.as_view()), name="blog_category"),
	path('add_blog_category', login_required(AddBlogCategory.as_view()), name="add_blog_category"),
	path('edit_blog_category/<int:cat_id>', login_required(EditBlogCategory.as_view()), name="edit_blog_category"),
	

	path('blog_list', login_required(BlogList.as_view()), name="blog_list"),
	path('add_blog', login_required(AddBlog.as_view()), name="add_blog"),


]