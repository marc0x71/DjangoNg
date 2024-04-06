from django.db import models

# Create your models here.
class ExampleModel(models.Model):
	firstname    = models.CharField(max_length=200)
	lastname     = models.CharField(max_length=200)

	def __str__(self):
		return self.lastname + ", " + self.firstname
