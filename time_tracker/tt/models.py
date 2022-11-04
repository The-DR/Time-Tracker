from django.db import models
from django.contrib.auth import get_user_model

class Time_Logs( models.Model ):
    user = models.ForeignKey( get_user_model(), on_delete=models.CASCADE )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    event = models.TextField()
    
    class Meta:
        verbose_name = 'Time Log'
        verbose_name_plural = 'Time Logs'
        
