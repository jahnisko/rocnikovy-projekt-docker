from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from helpdesk import settings
from django.views.generic import ListView
from .models import Dotaz, Poddotaz
from .forms import Kontaktuj, Prihlaseni
# Create your views here.


def index(request):
    '''send_mail(
        'Ahoj z Djanga',
        'Toto je automatická odpověď, že vše funguje, jak má :).',
        'vitezslav.jahn@post.cz',
        ['vita.domo@seznam.cz'],
        fail_silently=False
        )
    return render(request, 'index.html')
    '''
    if request.method == 'POST':
        form = Kontaktuj(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Neplatné')
            return redirect('/')
    form = Kontaktuj()
    return render(request, 'index.html', {'form': form})

'''
def prihlaseni(request):
    if request.method == 'POST':
        form = Prihlaseni(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            heslo = form.cleaned_data['heslo']
            try:
'''


class ProblemyListView(ListView):
    model = Dotaz
    template_name = 'vypis.html'
    context_object_name = 'dotaz'
