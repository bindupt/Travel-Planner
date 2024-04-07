from django import forms

from .models import  LocationModel


class Location_form(forms.ModelForm):

    class Meta:
        model=LocationModel
        fields=('district','Location','Description','Hw_to_reach')

