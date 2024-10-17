#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from .forms import ContactForm

def formulaire(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		sujet = form.cleaned_data['sujet']
		message = form.cleaned_data['message']
		envoyeur = form.cleaned_data['envoyeur']
		renvoi = form.cleaned_data['renvoi']
		envoi = True
	return render(request, 'formulaire/index.html', locals())