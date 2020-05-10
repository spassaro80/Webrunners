from django.urls import path
from .views import SignUpView,ProfileUpdate,EmailUpdate,ProfileListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/update/', EmailUpdate.as_view(), name='emailupdate'),
    path('profile/list', ProfileListView.as_view(), name='profil_list'),
]