from django import forms 
from django.forms import fields
from api.models import TodoNote
from django.forms import Form, ModelForm, DateField, widgets


class TodoForm(forms.ModelForm):
  class Meta:
    model = TodoNote
    fields = ['title','description','date_due','status','category']
    widgets = {
            'date_due': widgets.DateInput(attrs={'type': 'date'}),
        }