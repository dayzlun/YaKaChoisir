from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import EventForm
from .models import Event
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'index.html', context=None)


def connexion(request):
    return render(request, 'connexion.html', context=None)


class createEvent(TemplateView):
    def get(self, request, **kwargs):
        form = EventForm()
        args = {'form': form}
        return render(request, 'create_event.html', args)

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index.html')
        return HttpResponseRedirect('/create_event.html')


@login_required
def event(request):
    return render(request, 'event.html', context=None)


@login_required
def allEvent(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'user': request.user,
        'extra_data': request.user.social_auth.get(provider="epita").extra_data,
    }
    return render(request, 'all_event.html', context)
