# -*- coding: cp1252 -*-
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.staticfiles.templatetags.staticfiles import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from account.models import UserProfile
from form.codeForm import *
import urllib2
import datetime

def principal(request):
	return render_to_response('principal.html', RequestContext(request))

def loginform(request):
	return render_to_response('login_form.html', RequestContext(request))

def logout_view(request):
        logout(request)
        return render_to_response('principal.html', RequestContext(request))

    
def obtenerCodigo(url):
	urllib2.urlopen(url)
	
def loginMade(request):
        if request.method == 'POST':
                formLogin = LoginForm(request.POST)
                username = request.POST.get('username')
                password = request.POST.get('password')
            #Autenticamos al usuario con las lib de django
                user = authenticate(username=username, password=password)
                print user
                if user is not None:
                        if user.is_active:
                                login(request, user)
                        	return render_to_response('principal.html', RequestContext(request))
                        else:
                                print "Usuario nefasto"
                        
        else:
            formLogin = LoginForm()    
        return render_to_response('login_activate.html', {'formLogin': formLogin,} ,RequestContext(request))

#Redirect for buttons
def registerform(request):
        print "Vamos al formRegister"
        if request.method == 'POST':
                formRegister    = RegisterForm(request.POST)
                if formRegister.is_valid():
                        genero          = formRegister.cleaned_data['genero']
                        nombre          = formRegister.cleaned_data['nombre']
                        apellidos       = formRegister.cleaned_data['apellidos']
                        tipoDoc         = formRegister.cleaned_data['tipo_documento']
                        numeroDoc       = formRegister.cleaned_data['numero_documento']
                        user            = formRegister.cleaned_data['nombre_usuario']
                        password1       = formRegister.cleaned_data['password']
                        password2       = formRegister.cleaned_data['repassword']
                        email           = formRegister.cleaned_data['email']
                        if not password2:
                                raise ValidationError('Confirm Password', code='passConf')
                        if password1 != password2:
                                raise ValidationError('Match Password', code='passMatch')
                #Registramos el usuario !!
                        try:
                                User.objects.create_user(user, email, password1)
                                UserProfile.objects.create(genero=genero, nombre=nombre, apellidos=apellidos,
                                                   tipoDoc=tipoDoc, numeroDoc=numeroDoc, user=user,
                                                   email=email )
                        except:
                                raise ValidationError('User register', code='regisUser')

                else:
                        print "CASA"
                        
        else:
                formRegister = RegisterForm()
        return render_to_response('register_form.html',  {'formRegister': formRegister,} ,RequestContext(request))
 
def searchform(request):
        return render_to_response('search_form.html',  RequestContext(request))

def contact(request):
        return render_to_response('contacto.html',  RequestContext(request))
