# -*- coding: cp1252 -*-
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, PasswordInput
from django import forms

GENERE_CHOICES = (
         ('hombre','Hombre'),
         ('mujer','Mujer'),
        )
TIPDOC_CHOICES = (
        ('NIF', 'NIF'),
        ('NIE', 'NIE'),
        ('passp', 'Pasaporte'),
    )
        
class LoginForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField()
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

class RegisterForm(forms.Form):
        genero = forms.MultipleChoiceField(required=False, widget=forms.RadioSelect(attrs={'class':'input-xlarge'}), choices=GENERE_CHOICES,)
        nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Nombre'}))
        apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Apellidos'}))
        tipoDoc = forms.ChoiceField(widget=forms.Select(attrs={'class':'input-xlarge'}), choices=TIPDOC_CHOICES)
        numeroDoc = forms.CharField(widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Numero documento'}))
        user = forms.CharField(widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Usuario'}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-xlarge','placeholder':'Password'}), max_length=100)
        email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Email'}))
        
