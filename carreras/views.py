from django.shortcuts import render, get_object_or_404
from .models import runners,equipo,individual,carreras,carrera_activa
from django.db.models import Sum
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse,reverse_lazy
from .forms import formResult
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import IntegrityError

# Create your views here.

@method_decorator(login_required, name='dispatch')
class CarrerasListView(ListView):
    model = carreras
    
    def activa(self):
        return carrera_activa.objects.filter(status=True)

#Trying to refactor to a DetailView

@method_decorator(login_required, name='dispatch')
class CarrerasResultsDetailView(DetailView):
    model = carreras
    template_name = 'carreras/individual.html'
    context_object_name="resultados"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        carrera=carreras.objects.get(id=pk)
        resultados=individual.objects.filter(name=carrera)
        return resultados

    def datos_carreras(self):
        return carreras.objects.get(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datoscarreras']=carreras.objects.get(id=self.kwargs['pk'])
        return context

    def activa(self):
        return carrera_activa.objects.filter(status=True)


# @login_required
# def resultados(request,carreras_id):
#     nombres=runners.objects.all()
#     equipos=equipo.objects.all()
#     carrera=carreras.objects.get(id=carreras_id)
#     resultados=individual.objects.filter(name=carrera)
#     activa=carrera_activa.objects.filter(status=True)
#     return render(request, 'carreras/individual.html',{'nombres':nombres,'equipo': equipos, 'datos_carreras':carrera, 'resultados': resultados, 'carrera_activa': activa })

@method_decorator(login_required, name='dispatch')
class RunnersClassificationListView(ListView):
    model = runners
    template_name="carreras/general.html"
    context_object_name="resultados"
    
    def get_queryset(self):
        resultados=runners.objects.annotate(tot_score = Sum('individual__score')).order_by('-tot_score')
        return resultados
    
    def activa(self):
        return carrera_activa.objects.filter(status=True)

@method_decorator(login_required, name='dispatch')
class TeamsClassificationListView(ListView):
    model = runners
    template_name="carreras/equipos.html"
    context_object_name="resultados_equipos"

    def get_queryset(self):
        resultados_equipos=equipo.objects.annotate(tot_score = Sum('runners__individual__score')).order_by('-tot_score')
        return resultados_equipos
    
    def activa(self):
        return carrera_activa.objects.filter(status=True)


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
            return render(self.request, 'carreras/individual_form.html', {'form': form, 'int_mess' : int_mess})
        
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

