from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('feedback',views.feedback,name='feedback'),
    path('blog',views.blog,name='blog'),
    path('journal',views.journal,name='journal')
]