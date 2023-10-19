import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Game, Configuration


def index(request):
    context = {
        'games': Game.objects.all().order_by('start_time'),
        'configuration': Configuration.objects.first(),
    }
    return render(request, 'games/index.html', context)


def api(request):
    response = []
    for game in Game.objects.all().order_by('start_time'):
        response.append(
            {
                'championship': game.championship.name,
                'championship_image_url': game.championship.image_url,
                'home_team': game.home_team.name,
                'visiting_team': game.visiting_team.name,
                'home_team_image_url': game.home_team.image_url,
                'visiting_team_image_url': game.visiting_team.image_url,
                'start_time': f'{game.start_time.hour:>02}h{game.start_time.minute:>02}',
                'end_time': f'{game.end_time.hour:>02}h{game.end_time.minute:>02}',
                'is_live': game.is_live(),
                'is_finished': game.is_finished(),
                'buttons': [
                    {'url': b.url, 'name_in_page': b.name_in_page}
                    for b in game.watch_buttons.all()
                ],
            },
        )
    response.append({'header': Configuration.objects.first().header})
    return HttpResponse(json.dumps(response))
