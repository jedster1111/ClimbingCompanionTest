from django.shortcuts import render
from django.http import HttpResponse
from . models import Centre, Climb, Climber
from django.template import loader
from django.views import View

def listView(request):
    centre_list = Centre.objects.all()
    climb_list = Climb.objects.all()
    climber_list = Climber.objects.all()
    context = {
            'centre_list': centre_list,
            'climb_list': climb_list,
            'climber_list': climber_list,
        }

    template = loader.get_template('logbook/logbookList.html')

    return HttpResponse(template.render(context, request))
    # return HttpResponse('<h1>Hey this is the list View</h1>')

class listView2(View):

    def getContext(self):
        centre_list = Centre.objects.all()
        climb_list = Climb.objects.all()
        climber_list = Climber.objects.all()
        context = {
            'centre_list': centre_list,
            'climb_list': climb_list,
            'climber_list': climber_list,
        }
        return context

    def getTemplate(self):
        template = loader.get_template('logbook/logbookList.html')
        return template


    def get(self, request):
        return HttpResponse(self.getTemplate().render(self.getContext(), request))
        