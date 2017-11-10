from django.contrib import admin

from .models import Document, Comment, Question, Rec

admin.site.register(Document)
admin.site.register(Rec)
admin.site.register(Question)
admin.site.register(Comment)