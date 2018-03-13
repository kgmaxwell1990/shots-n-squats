from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_index
from accounts import urls as account_urls
from blog import urls as blog_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name="home"),
    url(r'^accounts/', include(account_urls)),
    url(r'^blog/', include(blog_urls)),
]
