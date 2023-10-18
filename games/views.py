from django.shortcuts import render

from .models import Championship


def index(request):
    context = {'championships': Championship.objects.all()}
    return render(request, 'games/index.html', context)
