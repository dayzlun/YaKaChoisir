from django import forms


class EvenForm(forms.Form):
    event_name = forms.CharField(label='Nom de l\'événement', max_length=64)
