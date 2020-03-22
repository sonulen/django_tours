from django.http import (Http404, HttpResponse)
from django.shortcuts import render
from django.views import View


class MainPageView(View):

    template_path = "main.html"

    def get(self, request):
        return render(
            request, self.template_path
        )


class TourPageView(View):

    template_path = "tours/tour.html"

    def get(self, request, id : int):
        return render(
            request, self.template_path
        )


class DeparturePageView(View):

    template_path = "tours/departure.html"

    def get(self, request, departure : str):
        return render(
            request, self.template_path
        )

def custom_404(request, exception):
    return render(request, '404.html')