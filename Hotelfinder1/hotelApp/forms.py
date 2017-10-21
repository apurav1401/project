from django import forms
class HotelForm(forms.Form):
    location = forms.DateField('location', None)
    check_in = forms.DateField('check_in', None)
    check_out = forms.DateField('check_out', None)



