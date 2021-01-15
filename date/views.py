from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def get_date(request):
    import datetime
    today = datetime.datetime.now().strftime('%A %d from the month of %B')
    return HttpResponse(today)

