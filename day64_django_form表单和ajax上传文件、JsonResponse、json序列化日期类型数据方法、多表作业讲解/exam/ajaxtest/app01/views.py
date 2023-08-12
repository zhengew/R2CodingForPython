import json
import os

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
from django.http import JsonResponse
# from ajaxtest.settings import BASE_DIR
from django.conf import settings # 全局 settings配置 引入配置项的时候建议使用全局配置，会先从用户的settings文件找，找不到会用全局配置
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
        elif request.path == '/home/':
            return render(request, 'home.html')
        elif request.path == "/data/": #  home 页面的 ajax请求
            l1 = [11, 22, 33]
            ret = request.GET.get('k1') # None
            print(request.get_full_path()) # get 数据 /data/?%7B%22k1%22:%22v1%22,%22k2%22:%22v2%22%7D
            # post 请求 json 格式 使用 reqeust.body 接收数据
            print(ret)
            return JsonResponse(l1, safe=False) # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        elif request.path == '/upload/':
            return render(request, 'upload.html')

    def post(self, request):
        if request.path == "/login/":
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # ajax 方式 data数据
            username = request.POST.get('uname')
            password = request.POST.get('pwd')
            if username == 'zew' and password == '123456':
                # ret = json.dumps({'code': 0, 'redirect_url': '/index/'})
                ret = {'code': 0, 'redirect_url': '/index/'}
                # return HttpResponse(ret, content_type="application/json")
                return JsonResponse(ret)
            else:
                # ret = json.dumps({"code":3,  "msg": "用户名或密码错误!"})
                ret = {"code":3,  "msg": "用户名或密码错误!"}
                # return HttpResponse(ret, content_type="application/json")
                return JsonResponse(ret)
        elif request.path == '/upload/':
            print(request.POST) # 拿到的是post请求的数据，但是文件相关数据需要用 request.FILES 去拿
            print(request.FILES) # <MultiValueDict: {'head-pic': [<InMemoryUploadedFile: 截屏2022-05-13 08.32.43.png (image/png)>]}>
            file_obj = request.FILES.get('head_pic') # 前端上传文件
            print(file_obj)
            file_name = file_obj.name
            path = os.path.join(settings.BASE_DIR, 'statics/img/', file_name) # 文件路径

            with open(path, 'wb') as f:
                # for i in file_obj: # 原生上传文件方法
                #     f.write(i)
                for chunk in file_obj.chunks():  # 上传文件 django 内置方法
                    f.write(chunk)

            return HttpResponse('200 ok')
