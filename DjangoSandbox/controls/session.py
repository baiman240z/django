from django.shortcuts import render, redirect
from django.contrib import messages


def sessions(request):
    if request.method == 'POST':
        request.session[request.POST.get('key')] = request.POST.get('value')
        messages.success(request, 'Saved')

    return render(request, 'session.html', {
        'sessions': request.session.items()
    })


def delete(request):
    if request.method == 'POST':
        request.session.pop(request.POST.get('key'))
        messages.success(request, 'Deleted')
    return redirect('/session')
