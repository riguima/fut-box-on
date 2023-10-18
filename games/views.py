from django.shortcuts import render

from .models import Championship, Configuration


def index(request):
    context = {
        'championships': Championship.objects.all(),
        'configuration': Configuration.objects.first(),
    }
    return render(request, 'games/index.html', context)
