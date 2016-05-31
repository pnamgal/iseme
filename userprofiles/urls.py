from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', views.authentication, name= 'authentication'),
    url(r'^registrar/$', views.verificar, name= 'verificar'),#en la url registrar..mira la funcion verificar
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^', views.hello, name= "hello"),
    
    ]  