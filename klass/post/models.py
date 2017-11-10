from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.URLField()
    context = models.TextField()
    is_active = models.BooleanField(default=True)
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title


class Rec(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.URLField()
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    link = models.URLField()
    context = models.TextField()
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title


# class Assignment(models.Model):
#     title = models.CharField(max_length=100)
#     link = models.URLField()
#     context = models.TextField()
#     deadline = models.DateTimeField()
#     comments = GenericRelation('Comment')
#
#     def __str__(self):
#         return self.title
#
#
# class SubmitAssignment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
#     assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL)
#     link = models.URLField()
#     context = models.TextField()
#
#     def __str__(self):
#         return f'{self.assignment.title} - {self.user.username}'


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    cotent_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    context = models.TextField()
