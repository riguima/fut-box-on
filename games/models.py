from datetime import datetime

from django.db import models


class Championship(models.Model):
    name = models.CharField()
    image_url = models.CharField()

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    name = models.CharField()
    image_url = models.CharField()

    def __str__(self) -> str:
        return self.name


class Game(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_team')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def is_live(self) -> bool:
        return self.start_time < datetime.now().time() < self.end_time
    
    def is_finished(self) -> bool:
        return datetime.now().time() > self.end_time

    def __str__(self) -> str:
        return f'{self.home_team} X {self.visiting_team}'


class WatchButton(models.Model):
    name = models.CharField()
    name_in_page = models.CharField(blank=True)
    url = models.CharField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Configuration(models.Model):
    header = models.CharField()
