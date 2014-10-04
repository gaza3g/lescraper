from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from django.db import IntegrityError
from django.utils.timezone import get_current_timezone
from django.conf import settings
from datetime import datetime
import requests
import sys
import csv
import time
import types
import collections
import parsedatetime
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import json
import datetime
import html

from jobapplications.models import JobStore, Company
from jobapplications.models import Job as JobModel

class Command(BaseCommand):

	help = 'Imports companies into our database'


	def __init__(self):
		self.base_url = 'http://www.indeed.com.sg'
		self.crawl_template = 'http://www.indeed.com.sg/jobs?q=developer&start='
		self.user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
		self.stop_value = settings.CRAWL_PAGES
		self.page_no = 0
		super().__init__()


	def handle(self, *args, **options):

		result = self.crawl()

		all_jobs = self.extract_info(result)

		'''
		delete all JobStore objects before this run
		'''
		JobStore.objects.all().delete()

		initial_job_count_str = str(JobModel.objects.count())
		initial_job_count = list(initial_job_count_str)
		initial_job_count = int(initial_job_count[0])

		'''
		populate JobStore table
		'''
		for job in all_jobs:

			js = JobStore(title=job.title,
							company=job.company,
							description=job.description,
							url=job.url,
							post_date=job.posted_on
				 )

			js.save()



		'''
		use the list of companies that we just crawled and use that to
		compare with our current company list and take only the ones
		that have not been added
		'''
		new_companies = JobStore.objects \
							.values('company') \
							.distinct() \
							.exclude(
									 company__in = Company.objects \
									 				.values_list('name', flat=True)
							) \
							.values_list('company', flat=True)

		'''
		Save each company into system
		'''
		for company in new_companies:
			c = Company(name=company, is_blacklisted=None)
			c.save()

		'''
		Save jobs into the system
		'''
		for js in JobStore.objects.all():
			c = Company.objects.get(name=js.company)
			j = c.job_set.create(
					title=js.title,
					description=js.description,
					url=js.url,
					post_date=js.post_date
				)

		new_job_count = int(JobModel.objects.count() - initial_job_count)
		new_companies_count = new_companies.count()

		return "%s | %s" % (new_job_count, new_companies_count)

		# self.stdout.write('%s new jobs added.' % int(JobModel.objects.count() - initial_job_count))
		# self.stdout.write('%s new companies added.' % new_companies.count())


	def crawl(self):

		results = []

		while self.page_no < self.stop_value:

			crawl_url = "{0}{1}".format(self.crawl_template,str(self.page_no))

			'''
			TODO: Add User-Agent
			'''

			page = urlopen(crawl_url)	
			data = page.read() 
			results.append(data)

			page.close()
			self.page_no = self.page_no + 10

			time.sleep(settings.CRAWL_EACH_PAGE_DELAY)

		return results


	def extract_info(self, result_list):

		all_jobs = []

		for item in result_list:
			soup = BeautifulSoup(item)
			postings = soup("div", itemtype="http://schema.org/JobPosting")
			for row in postings:
				company = row("span", itemprop="name")
				if company:
					company = company[0].string
				else:
					company = ""
				if not company:
					continue

				title = row("a", itemprop="title")[0]['title']
				url = self.base_url + row("a", itemprop="title")[0]['href']

				description = row("span", itemprop="description")[0].string

				if description is None:
					description = "No description available"

				cal = parsedatetime.Calendar()
				tz = get_current_timezone()
				post_date = cal.parse(row.find_all("span", "date")[0].string)
				posted_on_str = time.strftime("%Y-%m-%d", post_date[0])
				posted_on = tz.localize(datetime.datetime.strptime(posted_on_str, '%Y-%m-%d'))


				all_jobs.append(Job(title, company, description.strip(), url, posted_on))

		return all_jobs

class Job:
	def __init__(self, title, company, description, url, posted_on):
		self.title = title
		self.company = company
		self.description = description
		self.url = url
		self.posted_on = posted_on



