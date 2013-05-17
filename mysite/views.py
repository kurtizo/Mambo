# -*- coding: cp1252 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import urllib2
import datetime

def hello(request):
	return HttpResponse("Hello world")

def clock(request):
	now = datetime.datetime.now()
	html = "it is now %s." % now
	return HttpResponse(html)

def clockPlantilla(request):
	now = datetime.datetime.now()
	t = get_template('clockTPL.html')
	html = t.render(Context({'person_name': 'batman'}))
	return HttpResponse(html)

def obtenerCodigo(url):
	urllib2.urlopen(url)
	
	
