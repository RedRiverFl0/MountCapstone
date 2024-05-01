from django import forms
from .models import Person
from .models import Hire



class CalendarForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)


class PersonForm(forms.ModelForm): #creates the form class so that it can take the information from the form
    class Meta:
        model = Person # then creates the new class with the input names entered in the proper fields
        fields = ['firstName', 'lastName', 'email', 'phone', 'file']

class HireForm(forms.ModelForm):
    class Meta:
        model = Hire
        fields = ['firstName', 'lastName', 'email', 'phone', 'file']

