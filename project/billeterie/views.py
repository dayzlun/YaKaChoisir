from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ConnexionPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'connexion.html', context=None)


class CreateEventPageVew(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'create_event.html', context=None)
