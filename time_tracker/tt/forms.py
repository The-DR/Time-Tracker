from django.forms import ModelForm
from .models import Time_Logs

class Time_Logs_Form_B( ModelForm ):
    class Metta:
        fields = ( 'start_time', 'end_time', 'event' )
        model = Time_Logs

