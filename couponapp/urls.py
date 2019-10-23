from django.urls import path
from .views import *

urlpatterns = [
	path('types_of_use', login_required(TypesOfUse.as_view()), name="types_of_use"),
	path('keywords', login_required(Keywords.as_view()), name="keywords"),
	path('coupons', login_required(CouponList.as_view()), name="coupons"),
	path('add_coupon', login_required(AddCoupon.as_view()), name="add_coupon"),

]