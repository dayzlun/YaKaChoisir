# howdy/urls.py
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^connexion.html$', connexion, name="connexion"),
    url(r'^create_event.html$', createEvent.as_view(), name="createEvent"),
    url(r'^event.html$', event, name="event"),
    url(r'^index.html$', home, name="home"),
    url(r'^all_event.html$', allEvent, name="allEvent"),
    url(r'^compte.html$', compte, name="compte"),
    url(r'^inscription.html$', inscription, name="inscription"),
    url(r'^success.html$', success, name="success"),
    url(r'^api/$', api, name="api"),
    url(r'^ajax/get_events/$', getEvents, name="getEvents"),
    url(r'^test$', test, name="test"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
