from django.contrib import admin

from . import models


class WatchButtonLabelInline(admin.TabularInline):
    model = models.WatchButtonLabel


class GameAdmin(admin.ModelAdmin):
    inlines = [WatchButtonLabelInline]


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


class WatchButtonAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']



admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.Championship)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.WatchButton, WatchButtonAdmin)
admin.site.register(models.Configuration)
