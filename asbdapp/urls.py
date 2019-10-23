
from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage.as_view(), name="home"),
    path('new', New.as_view(), name="new"),
    path('custom', Custom.as_view(), name="custom"),
    path('used', Used.as_view(), name="used"),
    path('cart_invitation', MyCartInvitation.as_view(), name="cart_invitation"),
    path('mycart_tag', MyCartTag.as_view(), name="cart_tag"),
    path('mycart', MyCart.as_view(), name="mycart"),
    path('myorder', MyOrder.as_view(), name="myorder"),
    path('myorder_tag', MyOrderTag.as_view(), name="myorder_tag"),
    path('wishdrop', WishDropGreeting.as_view(), name="wishdrop"),
    path('aboutus', AboutUs.as_view(), name="aboutus"),
    path('whyus', WhyUs.as_view(), name="whyus"),
    path('faq', Faq.as_view(), name="faq"),
    path('contact_us', ContactUs.as_view(), name="contact_us"),
    path('terms', Terms.as_view(), name="terms"),
    path('privacy', Privacy.as_view(), name="privacy"),
    path('blog', Blog.as_view(), name="blog"),
    path('registration', Registration.as_view(), name="registration"),
    path('login', Login.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('forget_password', ForgetPassword.as_view(), name="forget_password"),
    path('reset_password', ResetPassword.as_view(), name="reset_password"),

 
]
