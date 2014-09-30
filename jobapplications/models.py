import datetime

from django.db import models
from django.utils import timezone

class Job(models.Model):

	title = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	post_date = models.DateTimeField('date posted')

	def was_published_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=7)

class Company(models.Model):

	name = models.CharField(max_length=255, unique=True) 
	is_blacklisted = models.NullBooleanField()

