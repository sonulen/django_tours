"""django_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, path
from django.views.generic.base import RedirectView

from tours.views import (
    MainPageView, TourPageView, DeparturePageView, custom_404
)

from django.conf import settings
from django.conf.urls.static import static

handler404 = custom_404


favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + '/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', MainPageView.as_view(), name='main'),
    path('tour/<int:id>/', TourPageView.as_view(), name='tour_detail'),
    path('departure/<str:departure>/',
         DeparturePageView.as_view(), name='departure_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
