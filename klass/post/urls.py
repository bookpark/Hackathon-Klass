from django.conf.urls import url

from post.views import document_list, rec_list, question_list

urlpatterns = [
    url(r'^document_list/$', document_list, name='document_list'),
    url(r'^rec_list/$', rec_list, name='rec_list'),
    url(r'^qst_list/$', question_list, name='question_list')
]
