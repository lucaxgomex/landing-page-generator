"""projeto_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# https://drive.google.com/drive/folders/13KlpjdV9S5FerjHi6EIZwygkmnloDfJQ

from django.contrib import admin
from django.urls import path, include
from alunos.views import home, cadastro, editar, excluir
from alunos.api.viewsets import AlunoViewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'aluno', AlunoViewsets, basename='Aluno')

# url, view, nome da url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('editar/<int:id>/', editar, name='editar'),
    path('excluir/<int:id>/', excluir, name='excluir'),
    path('api/', include(route.urls), name='api-alunos'),
]