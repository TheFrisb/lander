from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LanderView(TemplateView):
    template_name = 'lander/base.html'