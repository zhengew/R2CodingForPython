from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request, *args, **kwargs):

    if request.method == 'GET':
        return HttpResponse('200 ok')