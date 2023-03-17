from django.db import models

class UploadText(models.Model):
	name = models.CharField(max_length=200)
	humor = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class UploadImage(models.Model):
	title = models.CharField(max_length=200)
	caption = models.CharField(max_length=200)
	image = models.ImageField(upload_to='crazy_pics/')
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title