from django import forms
from django.forms import widgets


class RecordForm(forms.Form):
    author = forms.CharField(max_length=40, label='Автор', required=True)
    author_email= forms.EmailField( label='Email', required=True, widget=widgets.EmailInput)
    text = forms.CharField(max_length=3000, label='Текст', required=True, widget=widgets.Textarea)


