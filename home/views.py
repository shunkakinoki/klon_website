from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "home/index.html"

class ErrorPageView(TemplateView):
    template_name = "home/other/index-404.html"