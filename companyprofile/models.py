from django.db import models

# Create your models here.
class CompanyProfile(models.Model):
	company_name = models.CharField(max_length=200 )
	address = models.TextField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	Zip = models.CharField(max_length=15)
	telephone = models.CharField(max_length=15)
	email = models.EmailField(max_length=100)
	profile_pic = models.ImageField(upload_to = 'media')

	def __str__(self):
		return self.company_name