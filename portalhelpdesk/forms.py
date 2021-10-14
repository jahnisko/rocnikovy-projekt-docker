from django import forms
from django.contrib.auth import password_validation
from django.utils.safestring import mark_safe


class Prihlaseni(forms.Form):
    ''' Uživatelský email, pod kterým bude odesílat zprávu '''
    ''' Musí být Brano účet, protože se jedná pouze o smtp protokol Brano emailu '''
    email = forms.EmailField(max_length=100, label=mark_safe("<strong>Zadejte Váš email</strong>"))
    ''' Uživatelské heslo k emailu '''
    heslo = forms.CharField(
        label="Zadejte heslo",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )


class Kontaktuj(forms.Form):
    email = forms.EmailField(max_length=150, label=mark_safe("<strong>Zadejte email příjemce</strong>"))
    subject = forms.CharField(max_length=50, label=mark_safe("<strong>Zadejte předmět</strong>"))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), label=mark_safe("<strong>Zadejte zprávu</strong>"))