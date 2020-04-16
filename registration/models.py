from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 

# Create your models here.

#Función para borrar el fichero antiguo cuando se sube uno nuevo
def  custom_upload_to(instance,filename):
   old_instance=Profile.objects.get(pk=instance.pk)
   old_instance.avatar.delete()
   return 'profiles/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    link=models.URLField(max_length=200, null=True, blank=True)
    avatar=models.ImageField(upload_to='custom_upload_to', null=True, blank=True)
    best10km=models.TimeField(null=True, blank=True, verbose_name="Mejor marca 10km")
    best21km=models.TimeField(null=True, blank=True, verbose_name="Mejor marca 21km")
    best42km=models.TimeField(null=True, blank=True, verbose_name="Mejor marca 42km")
    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'
    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_created(sender,instance,**kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su contraseña")

