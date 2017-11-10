import re

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
    "DOC": "post:doc_qst_detail",
    "REC": "post:record_detail",
    "QST": "post:doc_qst_detail",
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
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse(TYPE_URL_MATCH[self.type], kwargs={'pk': self.pk})

    @staticmethod
    def get_youtube_id():
        pattern = re.compile(
            r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/ ]{11})',
            re.IGNORECASE)
        post = Post.objects.filter(type='REC')[0]
        url = post.link
        match = re.search(pattern, url)
        youtube_id = match.group(1)
        return youtube_id


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Post', null=True, blank=True)
    assignment = models.ForeignKey('assignments.Assignment', null=True, blank=True)
    submit_assignment = models.ForeignKey('assignments.SubmitAssignment', null=True, blank=True)
    context = models.TextField()

    def __str__(self):
        return f'{self.pk}'
