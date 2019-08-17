from django import forms
from .models import Contacts

'''
Contact form for prospective clients
'''
class AddContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'subject', 'message']
