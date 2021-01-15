from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def address_page(request):
    return HttpResponse('This is response page')
