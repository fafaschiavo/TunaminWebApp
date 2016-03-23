from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Audio_news(models.Model):
	title = models.CharField(max_length=400)
	short_description = models.CharField(max_length=400)
	link = models.CharField(max_length=400)
	original_link = models.CharField(max_length=400, default='-')
	image_link = models.CharField(max_length=400, default='-')

	def __title__(self):
		return self.title

	def __short_description__(self):
		return self.short_description

	def __link__(self):
		return self.link

	def __original_link__(self):
		return self.original_link

	def __image_link__(self):
		return self.image_link