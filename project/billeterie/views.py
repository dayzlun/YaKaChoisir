from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EventForm
from .models import Event
from django.http import HttpResponseRedirect


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class ConnexionPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'connexion.html', context=None)


class CreateEventPageVew(TemplateView):
    def get(self, request, **kwargs):
        form = EventForm()
        events = Event.objects.all()
        print(events)
        args = {'form': form, 'events': events}
        return render(request, 'create_event.html', args)

    def post(self, request, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index.html')
        return HttpResponseRedirect('/create_event.html')


class EventPageVew(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'event.html', context=None)
