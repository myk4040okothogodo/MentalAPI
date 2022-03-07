from django.db import models
from django.conf import settings
# Create your models here.


class therapycenter(models.Model):
    name = models.CharField(null= False, max_length=2255)
    candidates = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="patientsOfTheclinic", on_delete=models.CASCADE)
    location = models.CharField(max_length=255);
    therapists = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="caregiversofTheclinic",on_delete=models.CASCADE)



    def __str__(self):
        return self.name
 
