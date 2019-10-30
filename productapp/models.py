from django.db import models

# Create your models here.


class Product(models.Model):
	product_name = models.CharField(max_length=100)
	width = models.CharField(max_length=10)
	height = models.CharField(max_length=10)
	weight = models.CharField(max_length=10)
	price = models.CharField(max_length=10)
	process_time = models.CharField(max_length=10)
	backdrop_type = models.CharField(max_length=10)

	def __str__(self):
		return  self.product_name