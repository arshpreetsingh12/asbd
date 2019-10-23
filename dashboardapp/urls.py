
from django.urls import path
from .views import *

urlpatterns = [
	path('myaccount_info', MyAccountInfo.as_view(), name="myaccount_info"),
	path('myaccount_shipping', MyAccountShipping.as_view(), name="myaccount_shipping"),
	path('post_and_sale', PostAndSale.as_view(), name="post_and_sale"),
	path('manage_posting', ManagePosting.as_view(), name="manage_posting"),
	path('sales_order', SalesOrder.as_view(), name="sales_order"),
	path('order_history', OrderHistory.as_view(), name="order_history"),
]

