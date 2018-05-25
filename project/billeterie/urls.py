# howdy/urls.py
from django.conf.urls import url
from billeterie import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^connexion.html$', views.ConnexionPageView.as_view()),
    url(r'^create_event.html$', views.CreateEventPageVew.as_view()),
    url(r'^event.html$', views.EventPageVew.as_view())
]
