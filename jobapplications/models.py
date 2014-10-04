import datetime

from django.db import models
from django.utils import timezone

class Company(models.Model):

	name = models.CharField(max_length=255, unique=True) 
	is_blacklisted = models.NullBooleanField()
	

class Job(models.Model):

	title = models.CharField(max_length=255)
	company = models.ForeignKey(Company)
	description = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	post_date = models.DateTimeField('date posted')

	def was_published_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=7)

	def save(self, *args, **kwargs):

		existing = Job.objects \
						.filter(description=self.description, 
									post_date=self.post_date, 
										company=self.company, 
											title=self.title
								) \
						.exists()

		if not existing:
			super(Job, self).save(*args, **kwargs)


class JobStore(models.Model):

	title = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	url = models.CharField(max_length=255)
	post_date = models.DateTimeField('date posted')

class CrawlTask(models.Model):

	name = models.CharField(max_length=255)
	start_date = models.DateTimeField('start date')
	end_date = models.DateTimeField('end date')
	output = models.CharField(max_length=255)
