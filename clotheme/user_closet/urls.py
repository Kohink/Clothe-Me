from django.urls import path
from . import views

app_name = 'user_closet'

urlpatterns = [
    path('', views.indexx, name='indexx'),
    path('<int:closet_id>/', views.detail, name = 'detail'),
]