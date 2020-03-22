from django.http import (Http404, HttpResponse)
from django.shortcuts import render
from django.views import View

from tours.data import *

class MainPageView(View):

    template_path = "main.html"

    def get(self, request):
        return render(
            request, self.template_path
        )


class TourPageView(View):

    template_path = "tours/tour.html"

    def get(self, request, id : int):
        if id not in tours.keys():
            # Не нашли тура с таким id
            raise Http404
        
        return render(
            request, 
            self.template_path, 
            context={
                'tour': tours[id],
            }
        )


class DeparturePageView(View):

    template_path = "tours/departure.html"

    def get(self, request, departure : str):
        if departure not in departures.keys():
            # Такого направления нет
            raise Http404

        # Получим только туры по направлению
        # Вопрос: почему filtered_tours 
        # получается не отсортированный по ключам?
        filtered_tours = {
            key:tour for key, tour in tours.items() 
            if tour["departure"] == departure
            }


        return render(
            request, 
            self.template_path,
            context={
                'departure' : departure,
                'tours' : filtered_tours
            }
        )

def custom_404(request, exception):
    return render(request, '404.html')