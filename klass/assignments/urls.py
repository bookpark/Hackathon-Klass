from django.conf.urls import url

from .views import assignment_list, assignment_detail

urlpatterns = [
    url(r'^asm_list/$', assignment_list, name='assignment_list'),
    url(r'^asm_detail/(?P<pk>\d+)/$', assignment_detail, name='assignment_detail'),
]
