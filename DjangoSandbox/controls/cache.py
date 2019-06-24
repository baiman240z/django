from django.shortcuts import render, redirect
from django.core.cache import cache


def caches(request):
    keys = cache.get('cache_keys')
    if type(keys) is not list:
        keys = []

    if request.method == 'POST':
        keys.append(request.POST.get('key'))
        cache.set(
            request.POST.get('key'),
            request.POST.get('value'),
            int(request.POST.get('ttl'))
        )

    cache.set('cache_keys', keys, 86400)
    cache_items = cache.get_many(keys)

    return render(request, 'cache.html', {
        'caches': cache_items.items()
    })


def delete(request):
    if request.method == 'POST':
        cache.delete(request.POST.get('key'))
    return redirect('/cache')
