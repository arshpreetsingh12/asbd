from django.contrib import admin
from .models import *
from django.conf import settings

admin.site.register(BlogCategory)
admin.site.register(Blog)