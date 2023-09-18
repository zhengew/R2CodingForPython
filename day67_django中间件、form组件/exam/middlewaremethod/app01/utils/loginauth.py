# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: loginauth.py
# @datatime: 2023/9/18 08:11

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

from django.conf import settings

# 登录认证中间件
class LoginAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 白名单
        WHITE_URLS = settings.WHITE_URLS

        print(f'自定义中间件，请求:{request.path}')

        if request.path in WHITE_URLS:
            return None
        else:
            is_login = request.session.get('is_login')
            print(f'is_login: {is_login}, loginName:{request.session.get("loginName")}')
            if is_login:
                return None
            else:
                return redirect('login')





    def process_response(self, request, response):

        print(f'自定义中间件，响应: {request.path}')

        return response