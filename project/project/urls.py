from django.conf.urls import url, include
from django.contrib import admin
from social_django.urls import urlpatterns as social_django_urls
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include((social_django_urls, "social_django_app"), namespace='social')),
    url(r'^logout/', logout, {'next_page': '/connexion.html'}, name="logout"),
    url(r'^', include('billetterie.urls')),
]
