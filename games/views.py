import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Championship, Configuration


def index(request):
    context = {
        'championships': Championship.objects.all(),
        'configuration': Configuration.objects.first(),
    }
    return render(request, 'games/index.html', context)


def api(request):
    response = []
    for championship in Championship.objects.all():
        response.append(
            {
                'name': championship.name,
                'image_url': championship.image_url,
                'games': [
                    {
                        'home_team': g.home_team.name,
                        'visiting_team': g.visiting_team.name,
                        'home_team_image_url': g.home_team.image_url,
                        'visiting_team_image_url': g.visiting_team.image_url,
                        'start_time': f'{g.start_time.hour}h{g.start_time.minute}',
                        'end_time': f'{g.end_time.hour}h{g.end_time.minute}',
                        'is_live': g.is_live(),
                        'is_finished': g.is_finished(),
                        'buttons': [
                            {'url': b.url, 'name_in_page': b.name_in_page}
                            for b in g.watchbutton_set.all()
                        ]
                    }
                    for g in championship.game_set.all()
                ],
            }
        )
    response.append({'header': Configuration.objects.first().header})
    return HttpResponse(json.dumps(response))
