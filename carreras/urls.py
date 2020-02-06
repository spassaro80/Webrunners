from django.urls import path
from . import views 
from .views import IndividualCreate

urlpatterns = [
    path('resultados/<int:carreras_id>/', views.resultados, name="resultados"),
    path('', views.cursas, name="cursas" ),
    path('resultados/general/', views.general, name="general"),
    path('resultados/equipos/', views.equipos, name="equipos"),
    path('resultados/miposicion/', views.IndividualCreate.as_view(), name="miposicion"),
    path('resultados/miposicion/update', views.IndividualUpdate.as_view(), name="cambia_posicion"),
]