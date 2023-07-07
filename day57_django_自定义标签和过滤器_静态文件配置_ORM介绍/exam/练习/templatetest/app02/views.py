from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def app02Index(request):
    return HttpResponse('任务调度')