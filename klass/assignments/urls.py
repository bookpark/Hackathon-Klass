from django.conf.urls import url

from .views import assignment_list, assignment_detail, submit_assignment_list, submit_assignment_detail, assignment_add, \
    assignment_delete, submit_assignment_add, submit_assignment_delete

urlpatterns = [
    url(r'^asm_list/$', assignment_list, name='assignment_list'),
    url(r'^asm_detail/(?P<pk>\d+)/$', assignment_detail, name='assignment_detail'),
    url(r'^sub_asm_list/(?P<pk>\d+)/$', submit_assignment_list, name='submit_assignment_list'),
    url(r'^sub_asm_detail/(?P<pk>\d+)/$', submit_assignment_detail, name='submit_assignment_detail'),

    url(r'^asm_add/$', assignment_add, name='assignment_add'),
    url(r'^asm_delete/(?P<pk>\d+)/$', assignment_delete, name='assignment_delete'),
    url(r'^sub_asm_add/(?P<pk>\d+)/$', submit_assignment_add, name='submit_assignment_add'),
    url(r'^sub_asm_delete/(?P<pk>\d+)/$', submit_assignment_delete, name='submit_assignment_delete'),
]
