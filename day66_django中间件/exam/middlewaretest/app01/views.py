import os.path

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse

from utils.logUtils.logControl import DEBUG, INFO, ERROR
from common.setting import ConfigHandler

# Create your views here.


class App01Views(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/app01/':
            return redirect('home')
        elif request.path == '/app01/upload/':
            return render(request, 'upload.html')


    def post(self, request, *args, **kwargs):

        if request.path == '/app01/upload/':
            payload = request.POST.dict()
            DEBUG.logger.debug(f'文件上传payload: {payload}')
            files_obj = request.FILES.getlist('file')
            INFO.logger.info(f'file_obj: {files_obj}')
            DEBUG.logger.debug(f'文件上传，文件流: {files_obj}')

            try:
                for file in files_obj:
                    abs_path = os.path.join(ConfigHandler.file_path, file.name)
                    with open(abs_path, 'wb') as f:
                        for line in file:
                            f.write(line)
                ret = {"RETCODE": 200, "RETMSG": "SUCCESS"}
                INFO.logger.info(f'文件上传成功')
            except Exception as e:
                ret = {"RETCODE": "FILE_UPLOAD_ERROR", "RETMSG": "文件上传失败"}
                ERROR.logger.error(f'文件上传失败: {e}')

            return JsonResponse(ret)