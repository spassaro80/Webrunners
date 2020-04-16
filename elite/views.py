from django.shortcuts import render, get_object_or_404
from carreras.models import runners
from django.db.models import Sum
from django.views.generic.list import ListView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'elite/elite_home.html')


@method_decorator(login_required, name='dispatch')
class Ranking10Km(ListView):
    model = runners
    template_name = "elite/elite_tablescore.html"
    context_object_name="object_list"
    
    def get_queryset(self):
        if self.request.GET.get('q') == '10':
            object_list=runners.objects.exclude(user__profile__best10km = None ).order_by('user__profile__best10km')
        elif self.request.GET.get('q') == '21':
            object_list=runners.objects.exclude(user__profile__best21km = None ).order_by('user__profile__best21km')
        elif self.request.GET.get('q') == '42':
            object_list=runners.objects.exclude(user__profile__best42km = None ).order_by('user__profile__best42km')
        return object_list
