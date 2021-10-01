from django import forms
from .models import Listing

class CreateListingForm(forms.ModelForm):
    class Meta:
        model= Listing
        fields= '__all__'
        exclude= ['owner', 'list_date', 'is_published']


class UpdateListingForm(forms.ModelForm):
    class Meta:
        model= Listing
        fields= '__all__'
        exclude= ['owner', 'list_date']