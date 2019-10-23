from django.urls import path
from .views import *

urlpatterns = [
	path('price_and_fee', login_required(PriceAndFee.as_view()), name="price_and_fee"),
	path('manage_posting', login_required(ManagePosting.as_view()), name="manage_posting"),
	path('sales_data_custom', login_required(SalesDataCustom.as_view()), name="sales_data_custom"),
	path('sales_order', login_required(SalesOrder.as_view()), name="sales_order"),
	path('order_history', login_required(OrderHistory.as_view()), name="order_history"),

]