"""DjangoSandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from .controls import database, form, cache, session

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top, name='top'),
    path('form/input', form.input_form, name='form_input'),
    path('form/confirm', form.confirm),
    path('form/complete', form.complete),
    path('form/upload', form.upload, name='upload'),
    path('database/list', database.rows, name='db_rows'),
    path('database/form', database.form, name='db_form'),
    path('database/confirm', database.confirm),
    path('database/complete', database.complete),
    path('database/delete', database.delete),
    path('database/download', database.download),
    path('session', session.sessions, name='session'),
    path('session/delete', session.delete),
    path('cache', cache.caches, name='cache'),
    path('cache/delete', cache.delete),
    path('email', views.email, name='email'),
]
