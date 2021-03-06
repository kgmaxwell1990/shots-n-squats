from django.conf.urls import url, include
from . import urls_reset
from .views import *

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^profile/', profile, name="profile"),
    url(r'^register/', register, name="register"),
    url(r'^add_to_mailing_list/', add_to_mailing_list, name="add_to_mailing_list"),
    url(r'^password-reset/', include(urls_reset)),
]