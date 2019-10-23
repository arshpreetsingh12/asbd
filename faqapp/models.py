from django.db import models


class FAQCategory(models.Model):
	category_name = models.CharField(max_length = 100)
	sort_order = models.PositiveIntegerField()
	status = models.BooleanField(default = False)
	created_on = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.category_name + " : " + str(self.sort_order)


class FAQ(models.Model):
	category = models.ForeignKey(FAQCategory,on_delete = models.CASCADE)
	question = models.TextField()
	answer = models.TextField()
	sort_order = models.PositiveIntegerField()
	status = models.BooleanField(default = False)
	created_on = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return  self.question