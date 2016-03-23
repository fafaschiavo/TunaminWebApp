from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
	context = {}
	return render(request, 'index.html', context)

def TuneForMe(request):
	context = {}
	return render(request, 'tuneforme.html', context)

# return render(request, 'refresh-mastery-database.html', context)