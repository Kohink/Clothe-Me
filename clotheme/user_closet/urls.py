from django.urls import path
from . import views

app_name = 'user_closet'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('closet/add/', views.ClosetCreate.as_view(), name='closet-add'),
    path('closet/<int:pk>/', views.ClosetUpdate.as_view(), name='closet-update'),
    path('closet/<int:pk>/delete/', views.ClosetDelete.as_view(), name='closet-delete'),
    path('closet/<int:pk>/add/', views.ClothesCreate.as_view(), name='clothes-add'),
]