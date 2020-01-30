from django.shortcuts import render
from .models import runners,equipo,individual,carreras 
from django.db.models import Sum
from django.views.generic.edit import CreateView
from django.urls import reverse,reverse_lazy
from .forms import formResult
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

@login_required
def cursas(request):
    cursas=carreras.objects.all()
    return render(request, 'carreras\carreras.html',{'cursas':cursas})

@login_required
def resultados(request,carreras_id):
    nombres=runners.objects.all()
    equipos=equipo.objects.all()
    carrera=carreras.objects.get(id=carreras_id)
    resultados=individual.objects.filter(name=carrera)
    return render(request, 'carreras\individual.html',{'nombres':nombres,'equipo': equipos, 'datos_carreras':carrera, 'resultados': resultados })

@login_required
def general(request):
    resultados=runners.objects.annotate(tot_score = Sum('individual__score')).order_by('-tot_score')
    return render(request, 'carreras\general.html',{'resultados': resultados })

@login_required
def equipos(request):
    resultados_equipos=equipo.objects.annotate(tot_score = Sum('runners__individual__score')).order_by('-tot_score')
    return render(request, 'carreras\equipos.html',{'resultados_equipos': resultados_equipos})

@method_decorator(login_required, name='dispatch')
class IndividualCreate(CreateView):
    model = individual
    form_class = formResult

    def get_object(self):
        individual, created = Individual.objects.get_or_create(runners=self.request.user.runners)
        return individual

    def get_success_url(self):
        return reverse_lazy('general') + '?registered'

    def get_form_kwargs(self):
        kwargs = super(IndividualCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

