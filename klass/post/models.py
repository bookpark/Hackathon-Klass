from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse

POST_TYPE_CHOICE = (
    ("DOC", "강의자료",),
    ("REC", "강의녹화",),
    ("QST", "질문",),
    ("ASM", "과제",),
)

TYPE_URL_MATCH = {
    "DOC": "post:post_detail",
    "REC": "post:rec_detail",
    "QST": "post:qst_detail",
    "ASM": "post:asm_detail",
}


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=3, choices=POST_TYPE_CHOICE)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link = models.URLField(null=True, blank=True)
    context = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.type} || {self.title}'



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post')
    context = models.TextField()

    def __str__(self):
        return f'{self.post.title}-{self.user.username}'

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
