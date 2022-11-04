from django.shortcuts import render
from .models import Time_Logs


def home( request ):
    if request.method == 'POST':
        xyz         = request.POST.get( 'tst_txt' )
        start_time  = request.POST.get( 'start_time' )
        end_time    = request.POST.get( 'end_time' )
        event       = request.POST.get( 'event' )
        context = { 'cntxt': xyz, 
                    'start_time': start_time, 
                    'end_time': end_time, 
                    'event': event }
        logs = Time_Logs( start_time = start_time, end_time = end_time, event = event )
        log.save()
        return render( request, 'tt/home.html', context )
    
        
    return render( request, 'tt/home.html' )
