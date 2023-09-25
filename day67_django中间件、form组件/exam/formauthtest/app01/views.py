from django.shortcuts import render, HttpResponse, redirect
from django.views import View

# form组件
from app01.utils.registerform import RegisterForm

# Create your views here.

class App01View(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return redirect('login')

        elif request.path == '/login/':

            return render(request, 'login.html')

        elif request.path == '/register/':
            form_obj = RegisterForm()
            return render(request, 'register.html', {'form_obj': form_obj}) # form对象传递给响应对象

    def post(self, request, *args, **kwargs):

        if request.path == '/login/':
            data = request.POST.dict()
            print(data)

            return redirect('register')