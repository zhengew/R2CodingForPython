from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import View

from appRoot import models

from utils.logUtils.logControl import INFO
from utils.libUtils.libControl import get_md5
# Create your views here.

class AppRootViews(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return redirect('login')

        elif request.path == '/login/':
            return render(request, 'login.html')

        elif request.path == '/logout/':

            request.session.flush()
            return redirect('login')

        elif request.path == '/home/':
            return render(request, 'home.html')


    def post(self, request, *args, **kwargs):

        if request.path == '/login/':

            payload = request.POST.dict()
            INFO.logger.info(f'请求数据:{payload}')
            loginName = payload.get('username')
            loginPwd = payload.get('password')

            yn_loginName = models.UserInfo.objects.filter(username=loginName).exists()

            if yn_loginName:
                password = models.UserInfo.objects.get(username=loginName).password

                if password == get_md5(loginName, loginPwd):
                    ret = {"RETCODE": 200, "RETMSG": "success"}
                else:
                    ret = {"RETCODE": 'USERNAME_OR_PASSWORD_ERROR', "RETMSG": "用户名或密码错误"}
            else:
                ret = {"RETCODE": 'USERNAME_OR_PASSWORD_ERROR', "RETMSG": "用户名或密码错误"}

            # 设置 session
            if ret.get('RETCODE') == 200:
                request.session['username'] = loginName
                request.session['is_login'] = True

            return JsonResponse(ret)
