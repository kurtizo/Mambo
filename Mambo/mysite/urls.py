# -*- coding: cp1252 -*-
from django.conf.urls.defaults import patterns, include, url
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# USE (nombreWeb, nombreMethod)
urlpatterns = patterns	('', 
                                                ('^$', principal),
						('^inicio/$', principal),
						('^logout/$', logout_view),
						('^login/$', loginform), 
						('^actions/$', loginMade),
						('^register/$', registerform),
						('^search/$', searchform),
						('^contact/$', contact),
                         )
