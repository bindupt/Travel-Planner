from django import forms


from .models import  DistrictModel


class District_form(forms.ModelForm):

    class Meta:
        model=DistrictModel
        fields=('state','District','Area','Population','Altitude','Telcode','Description','Air','Rail','Road','Backwarter')







