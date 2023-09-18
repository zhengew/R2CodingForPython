import time

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse


from app01 import models
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
            # 删除 django_session 表后台数据和客户端 cookie
            request.session.flush()
            return redirect('login')

        elif request.path == '/register/':
            return render(request, 'register.html')

        elif request.path == '/home/':
            return render(request, 'home.html')


    def post(self, request, *args, **kwargs):

        if request.path == '/login/':

            payload = request.POST.dict()
            print(payload)

            loginName = payload.get('username', None)

            if models.UserInfo.objects.filter(username=loginName).exists():
                loginPwd = payload.get('password', None)
                password = models.UserInfo.objects.get(username=loginName).password

                if loginPwd == password:
                    ret = {"RETCODE": 200, "RETMSG": "success"}
                else:
                    ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": "用户名或密码错误"}
            else:
                ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": "用户名或密码错误"}

            # 登录成功，设置session
            if ret.get('RETCODE') == 200:
                request.session['loginName'] = loginName
                request.session['loginTime'] = time.time()
                request.session['is_login'] = True

            return JsonResponse(ret)

        elif request.path == '/register/':
            payload = request.POST.dict()
            username = payload.get('username')
            if models.UserInfo.objects.filter(username=username).exists():
                ret = {"RETCODE": "USERNAME_EXIST_ERROR", "RETMSG": "该用户已注册"}
            else:
                password = payload.get('password')
                r_password = payload.get('r_password')
                if password == r_password:
                    ret = {"RETCODE": 200, "RETMSG": "success"}
                    try:
                        models.UserInfo.objects.create(**{'username': username, 'password': password,})
                    except Exception as e:
                        ret = {"RETCODE": "REGISTER_ERROR", "RETMSG": "用户注册失败"}
                else:
                    ret = {"RETCODE": "PASSWORD_ERROR", "RETMSG": "两次密码输入不一致"}

            return JsonResponse(ret)