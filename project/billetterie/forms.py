from django import forms
from .models import Event, User, Userevent
import datetime


class UserEventForm(forms.ModelForm):
    billet_type = forms.IntegerField(required=False)
    inside = forms.NullBooleanField(required=False)
    staff = forms.NullBooleanField(required=False)
    user_id = forms.ModelChoiceField(queryset=User.objects.all())
    event_id = forms.ModelChoiceField(queryset=Event.objects.all())

    class Meta:
        model = Userevent
        fields = ['billet_type', 'inside', 'staff', 'user_id', 'event_id']


class UserForm(forms.ModelForm):
    email = forms.EmailField()
    email_ticket = forms.EmailField()
    password = forms.CharField(required=False)
    login = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    student = forms.NullBooleanField()
    access_level = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['email', 'email_ticket', 'password', 'login', 'firstname', 'lastname', 'student', 'access_level']


class EventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Nom de l\'événement', max_length=64)
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Description', max_length=64)
    start_date = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Date de début', initial=datetime.date.today)
    end_date = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Date de fin', initial=datetime.date.today)
    end_inscrip_date = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Date de fin d\'inscription', initial=datetime.date.today)
    max_place_student = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Nombre de places maximales internes')
    max_place_ext = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Nombre de places maximales externes')
    price_student = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Prix internes')
    price_extern = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Prix externes')
    display_available_places = forms.NullBooleanField()
    premium = forms.NullBooleanField()
    nb_places_student = forms.IntegerField()
    nb_places_extern = forms.IntegerField()

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'end_inscrip_date', 'max_place_student',
                  'max_place_ext', 'price_student', 'price_extern', 'display_available_places', 'premium',
                  'nb_places_student', 'nb_places_extern']
