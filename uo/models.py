from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Formation(models.Model):
    intitule=models.CharField(max_length=100,null=False)
    description=models.TextField(null=False)
    responsable=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.intitule
    
class UE(models.Model):
    
    titre = models.CharField(max_length=100)
    description = models.TextField()
    CM = models.PositiveIntegerField()  
    TD = models.PositiveIntegerField()  
    TP = models.PositiveIntegerField()  
    credits = models.PositiveIntegerField()  

    
    responsables = models.ManyToManyField('auth.User', blank=True)
    formations = models.ManyToManyField('Formation')

    def __str__(self):
        return self.titre