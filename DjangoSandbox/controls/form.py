from django.shortcuts import render, redirect
from django.conf import settings
import hashlib


def input_form(request):
    form = {
        'text': '',
        'textarea': '',
        'select': '',
        'radio': '',
        'checkbox': [],
    }

    if request.method == 'POST':
        form = {
            'text': request.POST.get('text'),
            'textarea': request.POST.get('textarea'),
            'select': request.POST.get('select'),
            'radio': request.POST.get('radio'),
            'checkbox': request.POST.getlist('checkbox'),
        }

    return render(request, 'form/input.html', {
        'selections': settings.APP_SETTINGS['selections'],
        'form': form,
    })


def confirm(request):
    if request.method == 'GET':
        return redirect('/form/input')

    form = {
        'text': request.POST.get('text'),
        'textarea': request.POST.get('textarea'),
        'select': request.POST.get('select'),
        'radio': request.POST.get('radio'),
        'checkbox': request.POST.getlist('checkbox'),
    }

    return render(request, 'form/confirm.html', {
        'selections': settings.APP_SETTINGS['selections'],
        'form': form,
    })


def complete(request):
    return render(request, 'form/complete.html')


def upload(request):
    params = {}
    if request.method == 'POST' and 'file' in request.FILES:
        params = {
            'posted': True,
            'name': request.FILES['file'].name,
            'bytes': request.FILES['file'].size,
            'type': request.FILES['file'].content_type,
            'sha256': hashlib.sha256(request.FILES['file'].read()).hexdigest(),
        }

    return render(request, 'form/upload.html', params)
