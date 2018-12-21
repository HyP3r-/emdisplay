from django.urls import path

import emdisplay.views.configuration
import emdisplay.views.events
import emdisplay.views.home
import emdisplay.views.messaging_templates
import emdisplay.views.parsing_templates
import emdisplay.views.receiver

# sites
urlpatterns = [
    path("", emdisplay.views.home.index, name="home-index"),
    path("configuration", emdisplay.views.configuration.index, name="configuration-index"),
    path("parsing-templates", emdisplay.views.parsing_templates.index, name="parsing-templates-index"),
    path("events", emdisplay.views.events.index, name="events-index"),
    path("receiver", emdisplay.views.receiver.index, name="receiver-index"),
    path("messaging-templates", emdisplay.views.messaging_templates.index, name="messaging-templates-index"),
]

# api
urlpatterns += [
    path("api/configuration", emdisplay.views.configuration.Configuration.as_view()),
]
