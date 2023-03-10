from django import forms
from listings.models import Band

class contactUsForm(forms.Form):
    name = forms.CharField(required = False, max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    class Meta:
        model = Band 
        fields = '__all__'