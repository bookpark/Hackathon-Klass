from django.conf.urls import url

from .views import document_list, record_list, question_list, document_question_detail, record_detail

urlpatterns = [
    url(r'^document_list/$', document_list, name='document_list'),
    url(r'^rec_list/$', record_list, name='rec_list'),
    url(r'^qst_list/$', question_list, name='question_list'),
    url(r'^doc_qst_detail/(?P<pk>\d+)/$', document_question_detail, name='doc_qst_detail'),
    url(r'^rec_detail/(?P<pk>\d+)/$', record_detail, name='record_detail'),
]
