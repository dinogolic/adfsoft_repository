from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback, name='feedback'),
    path('projekti', views.projekti, name='projekti'),
    path('usluge', views.usluge, name='usluge'),
    path('contact',views.contact, name='contact')
]