from django.core.management.base import BaseCommand, CommandError
from jobapplications.models import Job, Company
from django.utils import timezone
from django.db import IntegrityError

class Command(BaseCommand):

	help = 'Imports companies into our database'

	def handle(self, *args, **options):
		for job in Job.objects.all():
			c = Company(name=job.company, added_date=timezone.now())
			try:
				c.save()
			except IntegrityError as e:
				self.stdout.write(str(e))