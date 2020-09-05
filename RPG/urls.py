"""RPG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from RPJOGA.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^perfil/(?P<identificador>[A-Z,a-z,0-9]+)/detalhes', detalhes, name='detalhes'),
    url(r'^$', char_index),
    url(r'^pandora/', pandora),
    url(r'^perfil/', perfil),
    url(r'^char/', create_char),
    url(r'^enemy/', create_enemy),
    url(r'^perfil_inimigo/', perfil_inimigo),
    url(r'^logs/', logs),
    url(r'^invent_manage/', invent_manage),
    url(r'^create_skill/', create_skill),
    url(r'^create_minions/', create_minions),
] 
