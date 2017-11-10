from django.conf.urls import url

from .views import signup, signin, signout

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', signin, name='login'),
    url(r'^logout/$', signout, name='logout'),
]
