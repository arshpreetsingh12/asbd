from django.db import models

# Create your models here.

class Config(models.Model):

	site_name = models.CharField(max_length = 250)
	site_url = models.URLField()
	description = models.TextField()
	tags = models.CharField(max_length = 2000)
	youtube = models.URLField()
	facebook = models.URLField()
	twiiter = models.URLField()
	google  = models.URLField()
	logo = models.ImageField(upload_to = 'logo')
	maintaince_mode = models.BooleanField()

	def __str__(self):
		return self.site_name