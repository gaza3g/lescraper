from __future__ import absolute_import

from celery import shared_task
from jobapplications.management.commands.import_crawlresults import Command
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def crawl():
	co = Command()
	co.handle()