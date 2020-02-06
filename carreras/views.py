from django.shortcuts import render, get_object_or_404
from .models import runners,equipo,individual,carreras,carrera_activa
from django.db.models import Sum
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse,reverse_lazy
from .forms import formResult
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import IntegrityError

# Create your views here.

@login_required
def cursas(request):
    cursas=carreras.objects.all()
    activa=carrera_activa.objects.filter(status=True)
    return render(request, 'carreras\carreras.html',{'cursas':cursas, 'carrera_activa': activa})

@login_required
def resultados(request,carreras_id):
    nombres=runners.objects.all()
    equipos=equipo.objects.all()
    carrera=carreras.objects.get(id=carreras_id)
    resultados=individual.objects.filter(name=carrera)
    activa=carrera_activa.objects.filter(status=True)
    return render(request, 'carreras\individual.html',{'nombres':nombres,'equipo': equipos, 'datos_carreras':carrera, 'resultados': resultados, 'carrera_activa': activa })

@login_required
def general(request):
    resultados=runners.objects.annotate(tot_score = Sum('individual__score')).order_by('-tot_score')
    activa=carrera_activa.objects.filter(status=True)    
    return render(request, 'carreras\general.html',{'resultados': resultados, 'carrera_activa': activa })

@login_required
def equipos(request):
    resultados_equipos=equipo.objects.annotate(tot_score = Sum('runners__individual__score')).order_by('-tot_score')
    activa=carrera_activa.objects.filter(status=True)    
    return render(request, 'carreras\equipos.html',{'resultados_equipos': resultados_equipos, 'carrera_activa': activa})

# Vistas para gestionar las posiciones de un Runner en la clasificación

@method_decorator(login_required, name='dispatch')
class IndividualCreate(CreateView):
    model = individual
    form_class = formResult

    def get_success_url(self):
        return reverse_lazy('general') + '?registered'

    def get_form_kwargs(self):
        kwargs = super(IndividualCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
        
    def form_valid(self, form):
        form.instance.runners=self.request.user.runners
        try:
            return super().form_valid(form)
        except IntegrityError:
            int_mess= "Ya existe una posición para este Runner"
            return render(self.request, 'carreras\individual_form.html', {'form': form, 'int_mess' : int_mess})
        
        form.save()

@method_decorator(login_required, name='dispatch')
class IndividualUpdate(UpdateView):
    model = individual
    form_class = formResult
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('general') + '?updated'

    def get_form_kwargs(self):
        kwargs = super(IndividualUpdate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
    # def form_valid(self, form):
    #     form.instance.runners=self.request.user.runners
    #     try:
    #         return super().form_valid(form)
    #     except IntegrityError:
    #         int_mess= "Ya existe una posición para este Runner"
    #         return render(self.request, 'carreras\individual_form.html', {'form': form, 'int_mess' : int_mess})
        
    #     form.save()
    def get_object(self, queryset=None):
        carrera=carrera_activa.objects.get(status=True)
        return get_object_or_404(individual, name=carrera.name, runners=self.request.user.runners )

