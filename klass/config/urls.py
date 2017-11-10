from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .views import index
from member import urls as member_urls
from post import urls as post_urls
from assignments import urls as assignment_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include(member_urls, namespace='member')),
    url(r'^post/', include(post_urls, namespace='post')),
    url(r'^asm/', include(assignment_urls, namespace='assignment')),
    url(r'^$', index, name='index'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
