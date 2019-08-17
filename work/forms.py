from django import forms
from .models import Contacts


class AddContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'subject', 'message']
