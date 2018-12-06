from django.urls import path

import emdisplay.views.home
import emdisplay.views.configuration

urlpatterns = [
    path("", emdisplay.views.home.index, name="home-index"),
    path("configuration", emdisplay.views.configuration.index, name="configuration-index"),
]
