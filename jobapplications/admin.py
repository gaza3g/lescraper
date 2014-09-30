from django.contrib import admin
from jobapplications.models import Job, Company

class JobAdmin(admin.ModelAdmin):
	list_display = ('title', 'company', 'post_date')
	list_filter = ['post_date']
	search_fields = ['title', 'company']


class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Job,JobAdmin)
admin.site.register(Company,CompanyAdmin)

