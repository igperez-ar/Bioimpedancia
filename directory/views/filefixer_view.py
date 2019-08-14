from django.shortcuts import render
from django.views.generic import TemplateView


class FileFixerView(TemplateView):
    template_name = "filefixer.html"


