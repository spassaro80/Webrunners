from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail, EmailForm
from django import forms
from .models import Profile
from .forms import ProfileForm
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?registered'

    def get_form(self, form_class=None):
        form = super(SignUpView,self).get_form()
        #modificar formulario en tiempo de ejecución
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder' : 'e-mail'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder' : 'Repetir la contraseña'})
        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        form.fields['username'].help_text = ''
        form.fields['email'].help_text = ''
        form.fields['password1'].help_text = ''
        form.fields['password2'].help_text = ''

        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class=ProfileForm
    success_url=reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class=EmailForm
    success_url=reverse_lazy('profile')
    template_name = 'registration/email_update_form.html'

    def get_object(self):
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate,self).get_form()
        #modificar formulario en tiempo de ejecución
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder' : 'e-mail'})
        form.fields['email'].label = ''
        form.fields['email'].help_text = ''
        return form



