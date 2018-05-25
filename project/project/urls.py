from django.conf.urls import url, include
from django.contrib import admin
from social_django.urls import urlpatterns as social_django_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include((social_django_urls, "social_django_app"), namespace='social')),
    url(r'^', include('billeterie.urls')),
]
