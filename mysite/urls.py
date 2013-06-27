# -*- coding: cp1252 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# USE (nombreWeb, nombreMethod)
urlpatterns = patterns  ('', 
                           ('^$',index_view),
                           ('^inicio/$',index_view),
                           ('^login/$',login_view), 
                           ('^logout/$',logout_view),
                           ('^search/$',search_view),
                           ('^contact/$',contact_view),
                           ('^register/$',register_view),
                           ('^perfil/$',perfil_view),
                           ('^admin/', include(admin.site.urls)),
                           )
