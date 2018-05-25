from django import forms
from .models import Event


class EvenForm(forms.ModelForm):
    title = forms.CharField(label='Nom de l\'événement', max_length=64)
    description = forms.CharField(label='Description', max_length=64)
    start_date = forms.DateField(label='Date de début')
    end_date = forms.DateField(label='Date de fin')
    end_inscrip_date = forms.DateField(label='Date de fin d\'inscription')
    max_place_student = forms.IntegerField(label='Nombre de places maximales internes')
    max_place_ext = forms.IntegerField(label='Nombre de places maximales externes')
    price_student = forms.IntegerField(label='Prix internes')
    price_extern = forms.IntegerField(label='Prix externes')

    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'end_inscrip_date', 'max_place_student', 'max_place_ext', 'price_student', 'price_extern']
