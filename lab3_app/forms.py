from django import forms
from django.views.generic.edit import UpdateView
from .models import *


class AddShoesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Shoes
        fields = '__all__'

