from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# Create your views here.

# app01 cbv
class App01View(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return redirect('login')
        elif request.path == '/login/':
            return render(request, 'login.html')
        elif request.path == '/logout/':
            pass
        elif request.path == '/register/':
            return render(request, 'register.html')


    def post(self, request, *args, **kwargs):

        pass