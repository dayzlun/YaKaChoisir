# howdy/urls.py
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^connexion.html$', connexion, name="connexion"),
    url(r'^create_event.html$', createEvent.as_view(), name="createEvent"),
    url(r'^event.html$', event, name="event"),
    url(r'^index.html$', home, name="home"),
    url(r'^all_event.html$', allEvent, name="allEvent"),
    url(r'^compte.html$', compte, name="compte"),
]
