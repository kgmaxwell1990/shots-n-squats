from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_index, get_about, get_contact
from accounts import urls as account_urls
from blog import urls as blog_urls
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^about/$', get_about, name="about"),
    url(r'^contact/$', get_contact, name="contact"),
    url(r'^accounts/', include(account_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
