from django.db import models
from django.contrib.auth.models import User
import datetime
from django_countries.fields import CountryField
from django.conf import settings
# Create your models here.


class Profile(models.Model):
	user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	country = models.CharField(max_length=25,blank=True,null=True)
	state = models.CharField(max_length=25)
	terms_condition = models.BooleanField(null=True,blank=True,default=False)

	def __str__(self):
		return self.user.username


class ForgetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name='Code')

    def __str__(self):
        name = self.user.first_name + self.user.last_name
        return name

