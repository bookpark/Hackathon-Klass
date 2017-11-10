from django.conf.urls import url

from .views import document_list, record_list, question_list, document_question_detail, record_detail, comment_create, \
    question_upload, comment_delete, question_delete, post_create, rec_create

urlpatterns = [
    # post create
    url(r'^create/$', post_create, name='post_create'),
    url(r'^rec_create/$', rec_create, name='rec_create'),
    # list views
    url(r'^document_list/$', document_list, name='document_list'),
    url(r'^rec_list/$', record_list, name='rec_list'),
    url(r'^qst_list/$', question_list, name='question_list'),
    # detail views
    url(r'^doc_qst_detail/(?P<pk>\d+)/$', document_question_detail, name='doc_qst_detail'),
    url(r'^rec_detail/(?P<pk>\d+)/$', record_detail, name='record_detail'),
    # comment views
    url(r'^comment_create/(?P<post_pk>\d+)/$', comment_create, name='comment_create'),
    url(r'^comment_delete/(?P<comment_pk>\d+)/$', comment_delete, name='comment_delete'),
    # question views
    url(r'^question_upload/$', question_upload, name='question_upload'),
    url(r'^(?P<post_pk>\d+)/question_delete/$', question_delete, name='question_delete'),
]
