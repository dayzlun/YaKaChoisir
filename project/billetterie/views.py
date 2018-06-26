from email.mime.image import MIMEImage

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.utils.crypto import get_random_string
from django.core.mail import *

import qrcode
import os

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
    if not request.POST.get("var2"):
        return HttpResponseRedirect("index.html")
    event = Event.objects.get(title=request.POST.get("var2"))
    user = User.objects.get(login=request.user.username)
    if Userevent.objects.filter(event_id=event.title, user_id=user.email).exists():
        return HttpResponseRedirect('all_event.html')
    token = get_random_string(length=32)
    while Userevent.objects.filter(token=token).exists():
        token = get_random_string(length=32)
    form = UserEventForm({"user_id": user.email, "event_id": event.title, "token": token})
    if form.is_valid() and event.nb_places_student > 0:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(token)
        img = qr.make_image(fill_color="black", back_color="white")
        qrname = request.user.email + "-" + event.title + ".jpg"
        img.save(qrname)

        # Mail send
        html_content = render_to_string('email.html', context={"event": event}).strip()
        subject = "Confirmation d'inscription à " + event.title
        recipients = ["queiro_r@epita.fr"]
        reply_to = ['yakachoichoi@gmail.com']
        msg = EmailMultiAlternatives(
            subject,
            html_content,
            "Billetterie EPITA",
            recipients,
            reply_to=reply_to,
        )
        msg.content_subtype = "html"
        msg.mixed_subtype = 'related'
        msg.attach_file(qrname)
        msg.send()
        os.remove(qrname)

        form.save()
        event.nb_places_student -= 1
        event.save()
    return render(request, 'success.html')


def test(request):
    return render(request, 'success.html')


def api(request):
    token = request.GET.get("token")
    try:
        userevent = Userevent.objects.get(token=token)
    except Userevent.DoesNotExist:
        return JsonResponse("n", safe=False)
    if userevent.inside:
        userevent.inside = False
        userevent.save()
        return JsonResponse(["s", userevent.serializable_value("event_id"), userevent.serializable_value("user_id")],
                            safe=False)
    else:
        userevent.inside = True
        userevent.save()
        return JsonResponse(["e", userevent.serializable_value("event_id"), userevent.serializable_value("user_id")],
                            safe=False)


def inscription(request):
    name = request.POST.get("name")
    event = Event.objects.get(title=name)
    if event:
        if Userevent.objects.filter(event_id=name, user_id=request.user.email).exists():
            return render(request, 'inscription.html', {"event": event, "error": "Déjà inscrit"})
        elif not event.nb_places_student:
            return render(request, 'inscription.html', {"event": event, "noplace": "Plus de places"})
        else:
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
            form.image = form.cleaned_data['image']
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
            context = {
                'event': ev,
                'inscrit': Userevent.objects.filter(user_id=request.user.email, event_id=name).exists()
            }
        except Event.DoesNotExist:
            return render(request, 'event.html')
        if ev is not None:
            return render(request, 'event.html', context)
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
