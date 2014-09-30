from django.core.management.base import BaseCommand, CommandError
from jobapplications.models import Company
from django.utils import timezone
from django.db import IntegrityError
import csv
class Command(BaseCommand):

	help = 'Import crawl results.'

	def handle(self, *args, **options):
		blacklist = self.load_talks_from_csv()
		l = []
		for b in blacklist:
			try:
				c = Company.objects.filter(name=b)[:1].get()
				c.is_blacklisted = True
				c.save()
			except Company.DoesNotExist:
				continue

	def load_talks_from_csv(self):
		blacklist = []
		with open('filter.txt', 'r') as f:
			for line in f:
				blacklist.append(line.strip())

		return blacklist
