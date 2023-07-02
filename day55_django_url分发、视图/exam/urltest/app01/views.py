from django.shortcuts import render, HttpResponse

# Create your views here.

def app01_index(request):
    if request.method == 'GET':
        return HttpResponse('app01主页')
