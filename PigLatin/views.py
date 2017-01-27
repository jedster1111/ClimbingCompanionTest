from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def pigLatin(request):
    template = loader.get_template('pigLatin/pigLatin.html')

    return HttpResponse(template.render(request))
