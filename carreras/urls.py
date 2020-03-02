from django.urls import path
from . import views 
from .views import IndividualCreate,CarrerasListView,RunnersClassificationListView,TeamsClassificationListView,CarrerasResultsDetailView

urlpatterns = [
    path('resultados/<int:pk>/', views.CarrerasResultsDetailView.as_view(), name="resultados"),
    path('', views.CarrerasListView.as_view(), name="carreras" ),
    path('resultados/general/', views.RunnersClassificationListView.as_view(), name="general"),
    path('resultados/equipos/', views.TeamsClassificationListView.as_view(), name="equipos"),
    path('resultados/miposicion/', views.IndividualCreate.as_view(), name="miposicion"),
    path('resultados/miposicion/update', views.IndividualUpdate.as_view(), name="cambia_posicion"),
]