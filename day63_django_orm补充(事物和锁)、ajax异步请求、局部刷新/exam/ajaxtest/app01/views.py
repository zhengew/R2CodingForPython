import json

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
# Create your views here.

class LoginView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        if request.path == '/':
            return redirect(reverse('login'))
        elif request.path == '/login/':
            return render(request, 'login.html')
        elif request.path == '/index/':
            return render(request, 'index.html')

    def post(self, request):
        if request.path == "/login/":
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # ajax 方式 data数据
            username = request.POST.get('uname')
            password = request.POST.get('pwd')
            if username == 'zew' and password == '123456':
                ret = json.dumps({'code': 0, 'redirect_url': '/index/'})
                return HttpResponse(ret)
            else:
                ret = json.dumps({"code":3,  "msg": "用户名或密码错误!"})
                return HttpResponse(ret)