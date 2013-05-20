# -*- coding: cp1252 -*-
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response
from form.codeForm import *
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
        if request.method == 'POST':
            formLogin = LoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
        else:
            formLogin = LoginForm()    
        return render_to_response('login_activate.html', {'formLogin': formLogin,} ,RequestContext(request))

#Redirect for buttons
def registerform(request):
        print "Vamos al formRegister"
        if request.method == 'POST':
                formRegister = RegisterForm(request.POST)
        else:
                formRegister = RegisterForm()
        return render_to_response('register_form.html',  {'formRegister': formRegister,} ,RequestContext(request))
 
def searchform(request):
        return render_to_response('search_form.html',  RequestContext(request))

def contact(request):
        return render_to_response('contacto.html',  RequestContext(request))
