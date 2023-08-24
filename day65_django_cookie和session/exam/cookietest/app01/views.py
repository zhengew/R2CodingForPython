import os

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.utils.decorators import method_decorator # 装饰器
from django.conf import settings # 配置文件
from django.views import View

# Create your views here.

# 登录认证装饰器
def login_auth(func):

    def inner(request, *args, **kwargs):

        # 判断 cookie， 如果cookie 未携带或者 cookie过期，重定向到 login
        is_login = request.COOKIES.get('is_login') # cookie
        if is_login:
            ret = func(request, *args, **kwargs)
            return ret
        else:
            return redirect('login')
    return inner

class App01View(View):

    @method_decorator(login_auth)
    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/app01/':
            return redirect('home')

        elif request.path == '/app01/home/':
            return render(request, 'home.html')

        elif request.path == '/app01/upload/':
            return render(request, 'upload.html')

        elif request.path == '/app01/logout/':
            ret = redirect('login')
            ret.delete_cookie('is_login')
            return ret

    def post(self, request, *args, **kwargs):

        if request.path == '/app01/upload/':
            data = request.POST.dict()
            print(data)
            files = request.FILES.getlist('file')

            try:
                for file in files:
                    file_path = os.path.join(settings.BASE_DIR, 'statics', 'data', file.name)
                    with open(file_path, 'wb') as f:
                        for line in file:
                            f.write(line)
                ret = {"RETCODE": 200, "RETMSG": "SUCCESS"}
            except Exception as e:
                print(e)
                ret = {"RETCODE": "UPLOAD_ERROR", "RETMSG": "文件上传失败"}
            return JsonResponse(ret)
