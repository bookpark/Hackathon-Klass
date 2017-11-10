from django.conf.urls import url

from .views import assignment_list

urlpatterns = [
    url(r'^asm_list/$', assignment_list, name=assignment_list),
]
