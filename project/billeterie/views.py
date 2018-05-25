from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EvenForm
from django.http import HttpResponseRedirect


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ConnexionPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'connexion.html', context=None)


class CreateEventPageVew(TemplateView):
    def post(self, request, **kwargs):
        form = EvenForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/index.html')

    def get(self, request, **kwargs):
        form = EvenForm()
        return render(request, 'create_event.html', {'form': form})


class EventPageVew(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'event.html', context=None)
