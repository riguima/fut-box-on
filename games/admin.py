from django.contrib import admin

from . import models


class WatchButtonLabelInline(admin.TabularInline):
    model = models.WatchButtonLabel
    autocomplete_fields = ['watch_button']


class ChampionshipAdmin(admin.ModelAdmin):
    search_fields = ['name']


class GameAdmin(admin.ModelAdmin):
    inlines = [WatchButtonLabelInline]
    autocomplete_fields = ['championship', 'home_team', 'visiting_team']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


class WatchButtonAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Championship, ChampionshipAdmin)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.WatchButton, WatchButtonAdmin)
admin.site.register(models.Configuration)
