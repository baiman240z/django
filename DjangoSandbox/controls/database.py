from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from ..models import Hoge
from datetime import datetime
import csv


def rows(request):

    paginator = Paginator(Hoge.objects.all(), 10)
    no = request.GET.get('page')

    try:
        page = paginator.page(no)
    except PageNotAnInteger as e:
        print(e)
        page = paginator.page(1)
    except EmptyPage as e:
        print(e)
        page = paginator.page(paginator.num_pages)

    return render(request, 'database/list.html', {
        'page': page
    })


def form(request):
    if request.method == 'POST':
        params = {
            'id': request.POST.get('id'),
            'title': request.POST.get('title'),
            'body': request.POST.get('body'),
        }
    else:
        if request.GET.get('id'):
            try:
                row = Hoge.objects.get(id=request.GET.get('id'))
                params = {
                    'id': row.id,
                    'title': row.title,
                    'body': row.body,
                }
            except Hoge.DoesNotExist as e:
                print(e)
                return redirect('/database/list')
        else:
            params = {}

    return render(request, 'database/form.html', params)


def confirm(request):
    if request.method == 'GET':
        return redirect('/database/form')

    params = {
        'id': request.POST.get('id'),
        'title': request.POST.get('title'),
        'body': request.POST.get('body'),
    }

    return render(request, 'database/confirm.html', params)


def complete(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            row = Hoge.objects.get(id=request.POST.get('id'))
            row.title = request.POST.get('title')
            row.body = request.POST.get('body')
        else:
            row = Hoge.objects.create(
                title=request.POST.get('title'),
                body=request.POST.get('body'),
                created_at=datetime.now()
            )
        row.save()

    return redirect('/database/list')


def delete(request):
    if request.method == 'POST':
        try:
            row = Hoge.objects.get(id=request.POST.get('id'))
            row.delete()
        except Hoge.DoesNotExist as e:
            print(e)

    return redirect('/database/list')


def download(request):
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    response['Content-Description'] = 'hoge.csv'
    response['Content-Disposition'] = 'attachment; filename=hoge.csv'
    writer = csv.writer(response)
    for row in Hoge.objects.all():
        writer.writerow([
            row.id,
            row.title,
            row.body,
            row.created_at,
            row.updated_at,
        ])

    return response
