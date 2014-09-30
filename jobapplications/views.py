from django.http import Http404
from django.shortcuts import get_object_or_404, render

from jobapplications.models import Job

def index(request):
	latest_jobs_list = Job.objects.order_by('-post_date')
	ctx = {'latest_jobs_list': latest_jobs_list}
	return render(request, 
					'jobapplications/index.html', 
						ctx)

def block(request, job_id):
	job = get_object_or_404(Job, pk=job_id)
	return render(request, 'jobapplications/block.html', {'job': job})
