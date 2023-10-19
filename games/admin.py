from django.contrib import admin

from . import models


class GameAdmin(admin.ModelAdmin):
    autocomplete_fields = ['watch_buttons']


admin.site.register(models.Team)
admin.site.register(models.Championship)
admin.site.register(models.Game)
admin.site.register(models.WatchButton)
admin.site.register(models.Configuration)
