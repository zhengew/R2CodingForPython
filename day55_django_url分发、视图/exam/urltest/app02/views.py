from django.shortcuts import render, HttpResponse

# Create your views here.

def app02_index(request):
    if request.method == 'GET':
        return HttpResponse('app02主页')