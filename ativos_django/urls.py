from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),  # login/logout automáticos
    path('', include('estoque.urls')),              # suas rotas protegidas
]