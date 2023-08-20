from django.shortcuts import render, HttpResponse, redirect
from uploadfiletest.settings import BASE_DIR
from django.http import JsonResponse
import os

def index(request, *args, **kwargs):
    return redirect('upload')

def upload(request, *args, **kwargs):

    if request.method == 'GET':
        return render(request, 'upload.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        files_obj = request.FILES.getlist('file') # MultiValueDict对象
        print(files_obj)
        # 写入文件
        for file in files_obj:
            abs_path = os.path.join(BASE_DIR, 'statics', 'data', file.name) # 文件保存路径
            with open(abs_path, 'wb') as f:
                for chunk in file.chunks(): # 内置方法写入文件
                    f.write(chunk)

        return JsonResponse({'RETCODE': 200, 'RETMSG': '文件上传成功'})



