from django.urls import path
from . import views

urlpatterns = [ 
     path("i",views.handle_login,name="login"),
     path("",views.index,name="index"),
     path('lr', views.login_or_register, name='login_or_register'),
     path('l', views.dlog, name='dlog'),
     path("d",views.detail,name="detail"),
     path('contact', views.contact, name='contact'),
     path('info', views.info, name='info'), 
]

