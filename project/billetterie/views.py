from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import *
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')


def getEvents(request):
    date = request.GET.get('date', None)
    queryset = Event.objects.filter(start_date=date).values('title')
    return JsonResponse({"events": list(queryset)})


@login_required
def compte(request):
    form = UserForm({'email': request.user.email, 'email_ticket': request.user.email, 'login': request.user.username,
                     'firstname': request.user.first_name, 'lastname': request.user.last_name, 'student': True})
    if form.is_valid():
        form.save()
    context = {
        'user': request.user,
        'extra_data': request.user.social_auth.get(provider="epita").extra_data,
    }
    return render(request, 'compte.html', context)


def success(request):
    if request.POST.get("var1") == "ok":
        event = Event.objects.get(title=request.POST.get("var2"))
        user = User.objects.get(login=request.user.username)
        form = UserEventForm({"user_id": user, "event_id": event})
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return HttpResponseRedirect('success.html')


def inscription(request):
    name = request.POST.get("name")
    event = Event.objects.get(title=name)
    if event:
        return render(request, 'inscription.html', {"event": event})
    else:
        return HttpResponseRedirect('index.html')


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
        copy['nb_places_extern'] = copy['max_place_ext']
        copy['nb_places_student'] = copy['max_place_student']
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
        return render(request, 'all_event.html', {'events': events.order_by("start_date"), 'filter': filter})
    else:
        events = Event.objects.all().order_by("start_date")
        return render(request, 'all_event.html', {'events': events})
