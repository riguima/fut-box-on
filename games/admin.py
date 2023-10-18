from django.contrib import admin

from . import models


admin.site.register(models.Team)
admin.site.register(models.Championship)
admin.site.register(models.Game)
admin.site.register(models.WatchButton)
