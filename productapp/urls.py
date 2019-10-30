from django.urls import path
from .views import *

urlpatterns = [
	path('product_list', login_required(ProductList.as_view()), name="product_list"),
	path('add_product', login_required(AddProduct.as_view()), name="add_product"),
	path('edit_product/<product_id>', login_required(EditProduct.as_view()), name="edit_product"),
	path('shipping_list', login_required(ShippingList.as_view()), name="shipping_list"),
	path('add_shipping', login_required(AddShipping.as_view()), name="add_shipping"),

]