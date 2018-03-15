from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_blog, name="blog"),
    url(r'^view_post/(\d+)', view_post, name="view_post"),
    url(r'^new_post', new_post, name="new_post"),
    url(r'^edit_post/(\d+)', edit_post, name="edit_post")
]