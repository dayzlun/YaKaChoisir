# howdy/urls.py
from django.conf.urls import url
from billeterie import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^connexion.html$', views.ConnexionPageView.as_view()),
    url(r'^create_event.html$', views.CreateEventPageView.as_view()),
    url(r'^event.html$', views.EventPageView.as_view()),
    url(r'^index.html$', views.HomePageView.as_view()),
    url(r'^all_event.html$', views.AllEventPageView.as_view()),
]
