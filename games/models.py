from datetime import datetime

from django.db import models


class Championship(models.Model):
    name = models.CharField(verbose_name='nome')
    image_url = models.CharField(verbose_name='url da imagem')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonatos'


class Team(models.Model):
    name = models.CharField(verbose_name='nome')
    image_url = models.CharField(verbose_name='url da imagem')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'


class WatchButton(models.Model):
    name = models.CharField(verbose_name='nome')
    url = models.CharField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Botão Assistir'
        verbose_name_plural = 'Botões Assistir'


class Game(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name='campeonato')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team', verbose_name='time mandante')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_team', verbose_name='time visitante')
    start_time = models.TimeField(verbose_name='inicio')
    background = models.ImageField(upload_to='uploads', verbose_name='fundo', null=True)
    end_time = models.TimeField(verbose_name='final')

    def is_live(self) -> bool:
        return self.start_time < datetime.now().time() < self.end_time
    
    def is_finished(self) -> bool:
        return datetime.now().time() > self.end_time

    def __str__(self) -> str:
        return f'{self.home_team} X {self.visiting_team}'

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'


class WatchButtonLabel(models.Model):
    name = models.CharField(verbose_name='Nome na página')
    watch_button = models.ForeignKey(WatchButton, on_delete=models.CASCADE, verbose_name='Botão')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Jogo')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Botão Assistir'
        verbose_name_plural = 'Botões Assistir'


class Configuration(models.Model):
    header = models.CharField(verbose_name='cabeçalho')

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'
