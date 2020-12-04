from django.urls import path
from . import views

app_name = 'user_closet'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('closet/add/', views.ClosetCreate.as_view(), name='closet-add'),
]