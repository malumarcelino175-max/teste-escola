# Sequência certa
#python -m venv venv
#venv\Scripts\activate
#pip install django
#pip install -r requirements.txt ou pip freeze > requirements.txt
# django-admin startproject escola
#python manage.py startapp alunos
"""No settings.py:

Adicione 'alunos' em INSTALLED_APPS.

Configure TEMPLATES['DIRS'] = [BASE_DIR / "templates"].

Configure STATICFILES_DIRS = [BASE_DIR / "static"].

Configure LANGUAGE_CODE = 'pt-br' para usar o português do Brasil.
Configure TIME_ZONE = 'America/Sao_Paulo' para usar o fuso horário de São Paulo.
"""
"""Em escola/urls.py:

python
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("alunos/", include(("alunos.urls", "alunos"), namespace="alunos")),
]
"""
"""
Em alunos/urls.py:

python
from django.urls import path
from . import views

app_name = "alunos"

urlpatterns = [
    path("lista/", views.lista_view, name="lista"),
    path("novo/", views.novo_view, name="novo"),
    path("detalhe/", views.detalhe_view, name="detalhe"),
]
"""
"""Em alunos/views.py:

python
from django.shortcuts import render

def lista_view(request):
    return render(request, "alunos/lista.html")

def novo_view(request):
    return render(request, "alunos/novo.html")

def detalhe_view(request):
    return render(request, "alunos/detalhe.html")
"""

"""templates/base.html:
Estrutura com {% load static %}, logo, menu e rodapé.

templates/home.html:
Extende base.html e mostra mensagem de boas-vindas.

alunos/templates/alunos/lista.html:
Tabela com nomes fictícios, botão “Novo Aluno” e “Ver”.

alunos/templates/alunos/novo.html:
Formulário estático com Nome, Matrícula e Curso.

alunos/templates/alunos/detalhe.html:
Perfil estático de um aluno genérico."""

"""<a href="{% url 'alunos:lista' %}">Lista de Alunos</a>
<a href="{% url 'alunos:novo' %}">Novo Aluno</a>
<a href="{% url 'alunos:detalhe' %}">Ver Detalhes</a>
"""
"""
git init
git add .
git commit -m "Protótipo Gestão Escolar"
git branch -M main
git remote add origin https://github.com/seuusuario/escola.git
git push -u origin main
"""
"""
escola/                  # Projeto principal
│
├── escola/              # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── alunos/              # Aplicativo "alunos"
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── alunos/
│   │       ├── lista.html
│   │       ├── novo.html
│   │       └── detalhe.html
│   └── static/
│       └── alunos/
│           ├── css/
│           │   └── estilo.css
│           └── img/
│               └── logo.png
│
├── templates/           # Templates globais
│   ├── base.html
│   └── home.html
│
└── manage.py
"""
