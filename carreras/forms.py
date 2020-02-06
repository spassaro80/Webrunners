from .models import individual,carrera_activa
from django import forms
from django.shortcuts import render, get_object_or_404

class formResult(forms.ModelForm):
    class Meta:
        model = individual
        fields = ['name', 'number']#, 'runners']
        widgets= {
            'name' : forms.Select(attrs={'class' : 'form-control', 'placeholder': 'Indicar la carrera'}),
            'number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder': 'Indicar la posición'}),
            # 'runners' : forms.Select(attrs={'class' : 'form-control'}),

        }
        labels= {
            'name' : "Carrera",
            'number' : "Posición",
            # 'runners' : "Runner",            
        }
    
    # El Valor inicial del campo Carrera en el form es la carrera que está activa
    # Se pasa el valor request cambiando el kwargs en la vista y se usa el request.user en el form 

    def __init__(self,*args, **kwargs):
        carrera=get_object_or_404(carrera_activa,status=True)
        request=kwargs.pop("request")
        super(formResult,self).__init__(*args, **kwargs)
        if carrera is not None:
            self.fields['name'].initial =  carrera.name
        # self.fields['runners'].initial = request.user.runners

    # Si la carrera seleccionada no está activa, mensaje de error

    def clean_name(self):
        name=self.cleaned_data.get('name')
        if carrera_activa.objects.get(name=name).status==False:
            raise forms.ValidationError("Para la carrera seleccionada no se puede modificar la posición")
        return name
