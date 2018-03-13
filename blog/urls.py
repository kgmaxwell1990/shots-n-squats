from django.conf.urls import url
from .views import get_blog

urlpatterns = [
    url(r'^$', get_blog, name="blog"),
]