from django.urls import path
from . import views

urlpatterns = [
    path('', views.ativo_list, name='ativo_list'),  # 👈 isso aqui importa
    path('novo/', views.ativo_create, name='ativo_create'),
    path('editar/<int:pk>/', views.ativo_update, name='ativo_update'),
    path('excluir/<int:pk>/', views.ativo_delete, name='ativo_delete'),
]