# -*- coding: cp1252 -*-
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext

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
	
def login(request):
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('<h1>Page was found</h1>')
        else:
        # Show an error page
            return HttpResponseRedirect('<h1>batman</h1>')
        return t.render(Context({'person_name': 'batman'}))
