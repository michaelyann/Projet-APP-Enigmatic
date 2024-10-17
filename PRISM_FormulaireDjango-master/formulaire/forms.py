from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label = "Nom :")
    prenom = forms.CharField(max_length=100, label = "Prénom :")
    paysNaissance = forms.CharField(max_length=100, label = "Pays de naissance :")
    nationalite = forms.CharField(max_length=100, label = "Nationalité :")
    organismeAppartenance = forms.CharField(max_length=100, label = " Organisme d'appartenance :")
    fonction = forms.CharField(max_length=100, label = " Fonction :")
    personneVisite = forms.CharField(max_length=100, label = "Personne visitée :")