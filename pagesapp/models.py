from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=255,blank=True,null=True)
	content = models.TextField(blank=True,null=True)
	url=models.CharField(max_length=255,blank=True,null=True)
	status=models.BooleanField(default=True,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
