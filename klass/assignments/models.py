from django.conf import settings
from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    context = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class SubmitAssignment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)
    link = models.URLField(null=True, blank=True)
    context = models.TextField()

    def __str__(self):
        return f'{self.assignment.title} - {self.user.username}'
