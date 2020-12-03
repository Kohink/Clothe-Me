from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexx, name='indexx'),
    path('<int:closet_id>/', views.detail, name = 'detail'),
]