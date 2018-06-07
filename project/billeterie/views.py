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
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('connexion.html')
        return render(request, 'create_event.html')

    def post(self, request):
        copy = request.POST.copy()
        copy['display_available_places'] = 'display_available_places' in request.POST
        copy['premium'] = 'premium' in request.POST
        form = EventForm(copy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('all_event.html')
        else:
            context = {
                'form': form,
                'error': ''
            }
            return render(request, 'create_event.html', context)


@login_required
def event(request):
    name = request.GET.get('name')
    if name is not None:
        try:
            ev = Event.objects.get(title=name)
        except Event.DoesNotExist:
            return render(request, 'event.html')
        if ev is not None:
            return render(request, 'event.html', {'event': ev})
    return render(request, 'event.html')


@login_required
def allEvent(request):
    filter = request.GET.get('filter')
    if filter is not None:
        events = Event.objects.filter(title__contains=filter) | Event.objects.filter(description__contains=filter)
        return render(request, 'all_event.html', {'events': events, 'filter': filter})
    else:
        events = Event.objects.all()
        return render(request, 'all_event.html', {'events': events})
