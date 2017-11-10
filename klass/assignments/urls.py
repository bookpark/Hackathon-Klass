from django.conf.urls import url

from .views import assignment_list, assignment_detail, submit_assignment_list

urlpatterns = [
    url(r'^asm_list/$', assignment_list, name='assignment_list'),
    url(r'^asm_detail/(?P<pk>\d+)/$', assignment_detail, name='assignment_detail'),
    url(r'^sub_asm_list/(?P<pk>\d+)/$', submit_assignment_list, name='submit_assignment_list'),
]
