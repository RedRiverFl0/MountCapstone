from django import forms

class CalendarForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)