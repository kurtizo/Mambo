# -*- coding: cp1252 -*-
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response
import urllib2
import datetime

def hello(request):
	return HttpResponse("Hello world")

def clock(request):
	now = datetime.datetime.now()
	html = "it is now %s." % now
	return HttpResponse(html)

def loginform(request):
	return render_to_response('login_form.html', RequestContext(request))

def obtenerCodigo(url):
	urllib2.urlopen(url)
	
def loginMade(request):
	context = RequestContext(request)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        else:
            username = request.GET.get('username')
            password = request.GET.get('password')
        return render_to_response("login_activate.html",  context)
