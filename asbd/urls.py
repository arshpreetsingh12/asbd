from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from pagesapp.views import GetPages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('asbdapp.urls')),
    path('dashboard/',include('dashboardapp.urls')),
    path('admin/',include('adminpanelapp.urls')),
    path('faqapp/',include('faqapp.urls')),
    path('blogapp/',include('blogapp.urls')),
    path('salesapp/',include('salesapp.urls')),
    path('productapp/',include('productapp.urls')),
    path('imagesapp/',include('imagesapp.urls')),
    path('couponapp/',include('couponapp.urls')),
    path('pagesapp/',include('pagesapp.urls')),
    path('config',include('configuration.urls')),
    path('profile',include('companyprofile.urls')),

    path('<page>',GetPages.as_view()),

    path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)