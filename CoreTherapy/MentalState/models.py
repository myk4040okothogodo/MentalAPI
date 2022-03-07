from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _


class mentalState(models.Model):

    Nothappy         = 0
    Alittlehappy     = 3
    Moderatelyhappy  = 5
    Veryhappy        = 7
    Extremelyhappy   = 10

    HAPPY = ( 
            (Nothappy, _('no tinge of happiness')),
            (Alittlehappy, _('just a little bit of happiness')),
            (Moderatelyhappy, _('Avaragely happy')),
            (Veryhappy, _('Above avarage in hapiness lavel')),
            (Extremelyhappy, _('Very  very happy '))
            )

    Notstressed        = 0
    Alittlestressed    = 3
    Moderatelystressed = 5
    Verystressed       = 7
    Extremelystressed  = 10

    STRESS = (
             (Notstressed, _('not even a little ounce of stress')),
             (Alittlestressed, _('just alittle bit of stress')),
             (Moderatelystressed, _('Experiencing avarage amount of stress')),
             (Verystressed, _('Experiencing an above average amount of stress')),
             (Extremelystressed, _('Experiencing an extremely high amount of stress'))
            )


    Notactive        = 0
    Alittleactive    = 3
    Moderatelyactive = 5
    Veryactive       = 7
    Extremelyactive  = 10
    ACTIVE = (
            (Notactive, _('Not being even a little bit active')),
            (Alittleactive, _('Being a little active ')),
            (Moderatelyactive, _('Being avaragely active today')),
            (Extremelyactive, _('Iam extremely active today')),
                            
            )


    activitylevel = models.SmallIntegerField(choices= ACTIVE, default=Notactive)
    stresslevel  = models.SmallIntegerField(choices= STRESS, default=Notstressed)
    happinesslevel = models.SmallIntegerField(choices= HAPPY, default=Nothappy)
    candidate = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="candidatefor_therapy", on_delete= models.CASCADE)
    therapist = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="therapy_administor", on_delete=models.CASCADE)
    dateOflogging = models.DateTimeField(auto_now_add=True)
    candidates_note  = models.TextField()



    def __str__(self):
        return self.candidates_note


