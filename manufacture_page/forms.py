from .models import Manu
from django.forms import ModelForm

class ManuForm(ModelForm):
    class Meta:
        model= Manu
        fields = ['name', 'phone', 'email', 'query']