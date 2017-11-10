from django.contrib import admin

from .models import Assignment, SubmitAssignment

admin.site.register(Assignment)
admin.site.register(SubmitAssignment)