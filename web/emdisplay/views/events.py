from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, "emdisplay/events.html")


class Events(View):
    def get(self, request):
        return JsonResponse({})

    def post(self, request):
        return JsonResponse({})
