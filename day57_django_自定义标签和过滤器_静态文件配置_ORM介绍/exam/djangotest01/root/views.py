from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.utils.decorators import method_decorator  # 装饰器

class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.body)
        print(username, password)
        if username == 'zew' and password == '123':
            return render(request, 'home.html')
        else:
            return HttpResponse('用户名或密码错误！')
