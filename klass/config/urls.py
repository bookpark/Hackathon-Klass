from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from member import urls as member_urls
from post import urls as post_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^member/', include(member_urls, namespace='member')),
    url(r'^post/', include(post_urls, namespace='post')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
