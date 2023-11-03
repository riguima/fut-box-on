from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('api', views.api),
    path('api/watchbuttons', views.watch_buttons),
]
