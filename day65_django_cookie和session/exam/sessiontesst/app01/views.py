import os

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django.utils.decorators import method_decorator # 装饰器
from django.conf import settings
# Create your views here.

def login_auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login')
        if is_login == True:
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
        if request.path == '/app01/home/':
            return render(request, 'home.html')

        elif request.path == '/app01/upload/':
            return render(request, 'upload.html')

    def post(self, request, *args, **kwargs):

        if request.path == '/app01/upload/':
            data = request.POST.dict()
            files_obj = request.FILES.getlist('file')
            print( files_obj)
            try:
                for file in files_obj:
                    file_path = os.path.join(settings.BASE_DIR, 'statics', 'data', file.name)
                    print(file_path)
                    with open(file_path, 'wb') as f:
                        for line in file:
                            f.write(line)
                ret = {"RETCODE": 200, "RETMSG": "SUCCESS"}
            except Exception as e:
                print(e)
                ret = {"RETCODE": "UPLOAD_ERROR", "RETMSG": "文件上传失败"}

            return JsonResponse(ret)
