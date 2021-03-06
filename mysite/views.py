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

#P�gina principal
def index_view(request):
	return render_to_response('principal.html', RequestContext(request))

#Cerramos la sesi�n
def logout_view(request):
        logout(request)
        return render_to_response('principal.html', RequestContext(request))

	
def login_view(request):
	
        if request.method == 'POST':
                formLogin = LoginForm(request.POST)
                username = request.POST.get('username')
                password = request.POST.get('password')
            #Autenticamos al usuario con las lib de django
                user = authenticate(username=username, password=password)
                if user is not None:
                        if user.is_active:
								print "Usuario esta activo"
								profiles = UserProfile.objects.all()
							#	apellidos = UserProfile.objects.get(apellidos)
								print "nombre" + str(profiles)
							#	request.profile = profile
								login(request, user)
								return render_to_response('principal.html', RequestContext(request))
                        else:
                                print "Usuario nefasto"
                        
        else:
            formLogin = LoginForm()    
        return render_to_response('login_activate.html', {'formLogin': formLogin,} ,RequestContext(request))

#Vista del registro
def register_view(request):

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
                        #Se crea el usuario
                        User.objects.create_user(user, email, password1)
                        #Se crea el perfil del usuario
                        UserProfile.objects.create(genero=genero, nombre=nombre, apellidos=apellidos,
                                                   tipoDoc=tipoDoc, numeroDoc=numeroDoc, user=user,
                                                   email=email )
                        
                        return render_to_response('principal.html', RequestContext(request))
                        
        else:
                formRegister = RegisterForm()

        return render_to_response('register_form.html',  {'formRegister': formRegister,} ,RequestContext(request))
 
#Vista del men� de b�squeda
def search_view(request):
        return render_to_response('search_form.html',  RequestContext(request))

#Vista del men� de contacto
def contact_view(request):
        return render_to_response('contacto.html',  RequestContext(request))

#Vista del men� de perfil
def perfil_view(request):
        return render_to_response('perfil.html',  RequestContext(request))
