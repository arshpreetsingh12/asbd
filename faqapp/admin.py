from django.contrib import admin
from .models import *
from django.conf import settings
# Register your models here.
admin.site.register(FAQCategory)
admin.site.register(FAQ)