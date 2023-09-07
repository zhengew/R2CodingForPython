from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.


class App01Views(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/app01/':
            return redirect('home')



    def post(self, request, *args, **kwargs):
        pass