from django.db import models

# Create your models here.
class Todo(models.Model):
	#Model to store creation date of item
	added_date = models.DateTimeField()
	#Model to store item 
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text