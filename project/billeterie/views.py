from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import EventForm
from .models import Event


# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required
def compte(request):
    context = {
        'user': request.user,
        'extra_data': request.user.social_auth.get(provider="epita").extra_data,
    }
    return render(request, 'compte.html', context)


def connexion(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('compte.html')
    else:
        return render(request, 'connexion.html')


class createEvent(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'create_event.html')

    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html')
        return render(request, 'create_event.html', {'form': form})


@login_required
def event(request):
    return render(request, 'event.html')


@login_required
def allEvent(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'all_event.html', context)
