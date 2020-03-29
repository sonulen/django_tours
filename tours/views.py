from django.http import (Http404, HttpResponse)
from django.shortcuts import render
from django.views import View
from tours.data import (subtitle, description, departures, tours)
from random import shuffle

class MainPageView(View):

    template_name = "main.html"

    def get(self, request):
        # Перемешаем словарь туров.
        # Т.к. shuffle умеет работать только с list
        # Возьмем лист из ключей от tours - перемешаем его
        # На его основе сгенерим новый словарь
        shuffled_keys = list(tours.keys())
        shuffle(shuffled_keys)
        shuffled_tours = dict((key,tours[key]) for key in shuffled_keys[:6])

        return render(
            request, 
            self.template_name,
            context={
                'subtitle' : subtitle,
                'description' : description,
                'tours': shuffled_tours,
            }
        )


class TourPageView(View):

    template_name = "tours/tour.html"

    def get(self, request, id: int):
        if id not in tours.keys():
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                'from': departures[tours[id]["departure"]],
                'tour': tours[id],
            }
        )


class DeparturePageView(View):

    template_name = "tours/departure.html"

    def get(self, request, departure: str):
        if departure not in departures.keys():
            raise Http404

        filtered_tours = {
            key: tour for key, tour in tours.items()
            if tour["departure"] == departure
        }

        return render(
            request,
            self.template_name,
            context={
                'departure': departure,
                'tours': filtered_tours
            }
        )


def custom_404(request, exception):
    return render(request, '404.html')
