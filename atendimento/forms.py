from django import forms

from .models import atender


class formulario_atend(forms.ModelForm):

    class Meta:
        model = atender
        exclude = ()

        widgets = {
            'atendimento': forms.DateInput(attrs={"type": "date"}),
        }
