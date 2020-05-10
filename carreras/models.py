from django.db import models
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User

# Create your models here.

class equipo(models.Model):
    name=models.CharField(verbose_name="Equipo", max_length=100, unique=True, null=False)
    color=models.CharField(verbose_name="Color", max_length=100)
        
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.name

class runners(models.Model):
    SEX = [
    ('H', 'Hombre'),
    ('M', 'Mujer'),
]
    name=models.CharField(verbose_name="Nombre", max_length=100,null=False)
    surname=models.CharField(verbose_name="Apellido", max_length=100,null=False)
    sex=models.CharField(verbose_name="Sexo", max_length=2,null=False, choices=SEX)
    team=models.ForeignKey('equipo', on_delete=models.CASCADE,null=False)
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)


    class Meta:
        verbose_name = 'Runner'
        verbose_name_plural = 'Runners'

    def __str__(self):
        return self.name +  " " + self.surname

    def is_elite(self):
        if self.user.profile.best10km and self.user.profile.best21km == None and self.user.profile.best42km == None:
            return False
        return True
        

        
class carreras(models.Model):
    name=models.CharField(verbose_name="Nombre", max_length=100, unique_for_date="date",null=False)
    date=models.DateField(verbose_name="Fecha",null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="carreras", verbose_name="Imagen", blank=True, null=True)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creación")
    modified = models.DateField(auto_now=True, verbose_name="Fecha edición")

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        #ordering = ['-created']

    def __str__(self):
        return self.name

class individual(models.Model):
    name=models.ForeignKey('carreras', verbose_name="Nombre", max_length=100,null=False, on_delete=models.CASCADE)
    number=models.SmallIntegerField(verbose_name="Posición",null=False)
    runners=models.ForeignKey('runners', on_delete=models.CASCADE,null=False)
    score=models.SmallIntegerField('Puntuación', null=False)


    class Meta:
        verbose_name = 'Clasificación Individual'
        verbose_name_plural = 'Clasificación Individual'
        ordering = ['number']
        unique_together = (("name", "number"),("name", "runners"), ("name", "runners" ,"number"))


    def __str__(self):
        return str(self.name)        

#actualizar la puntuación en función de la clasificación cada vez que se guarda una instancia nueva

@receiver(pre_save, sender=individual)
def update_score(sender, instance, **kwargs):
    if instance.number is None:
        newscore =  0
    if instance.number < 9:
        newscore =  200 - (instance.number - 1) * 5
    else:
        newscore =  165 - (instance.number -8) * 2
    instance.score=newscore
    instance.save
    return instance 

class carrera_activa(models.Model):
    name=models.ForeignKey('carreras', max_length=100,null=False, on_delete=models.CASCADE)
    status=models.BooleanField(verbose_name="Carrera Activa", null=False, default=False)
    def __str__(self):
        return str(self.name)  