from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator # 装饰器

# Create your views here.

class App01View(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        pass

    def post(self, request, *args, **kwargs):

        pass