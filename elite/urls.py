from django.urls import path
from . import views 
from .views import home,Ranking10Km

elite_patterns = ([
    path('', views.home, name="home"),
    path('best10/', Ranking10Km.as_view(), name='best'),
],'elite')