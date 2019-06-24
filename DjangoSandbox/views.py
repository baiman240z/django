from django.shortcuts import render
from django.core.mail import send_mail


def top(request):
    return render(request, 'top.html')


def email(request):
    params = {
        'message': False,
    }

    if request.method == 'POST':
        send_mail(
            request.POST.get('subject'),
            request.POST.get('body'),
            request.POST.get('sender'),
            [request.POST.get('receiptto')]
        )
        params['message'] = 'your email has been sent'
        params['subject'] = request.POST.get('subject')
        params['body'] = request.POST.get('body')
        params['sender'] = request.POST.get('sender')
        params['receiptto'] = request.POST.get('receiptto')

    return render(request, 'email.html', params)
