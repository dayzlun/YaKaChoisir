from django import forms
from .models import Event
import datetime


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

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'end_inscrip_date', 'max_place_student',
                  'max_place_ext', 'price_student', 'price_extern', 'display_available_places', 'premium']
