from django.contrib import admin

from . import models


class WatchButtonLabelInline(admin.TabularInline):
    model = models.WatchButtonLabel


class GameAdmin(admin.ModelAdmin):
    inlines = [WatchButtonLabelInline]


admin.site.register(models.Team)
admin.site.register(models.Championship)
admin.site.register(models.Game, GameAdmin)
admin.site.register(models.WatchButton)
admin.site.register(models.Configuration)
