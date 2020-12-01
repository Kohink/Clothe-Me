from django.urls import path
from . import views

urlpatterns = [
    path('', views.indd, name='indd'),
]