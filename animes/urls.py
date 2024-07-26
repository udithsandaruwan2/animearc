from django.urls import path
from . import views

urlpatterns = [
    path('', views.animes, name='animes'),
    path('btth/', views.btth, name='btth'),
    path('epi/', views.singleEpi, name='single-epi'),
]
