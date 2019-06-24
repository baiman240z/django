from django.shortcuts import render, redirect


def sessions(request):
    if request.method == 'POST':
        request.session[request.POST.get('key')] = request.POST.get('value')

    return render(request, 'session.html', {
        'sessions': request.session.items()
    })


def delete(request):
    if request.method == 'POST':
        request.session.pop(request.POST.get('key'))
    return redirect('/session')
