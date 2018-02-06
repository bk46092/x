from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'xie/index.html', {'title': 'Czołem stara kurwo'})

def imie(request, name):
	agent = request.META['HTTP_USER_AGENT']
	return HttpResponse("Aloha {}. To jest {}".format(name, agent))
