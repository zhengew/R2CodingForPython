# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: loginauth.py
# @datatime: 2023/9/18 08:11

from django.utils.deprecation import MiddlewareMixin

# 登录认证中间件
class LoginAuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        print(f'自定义中间件，请求:{request.path}')

    

    def process_response(self, request, response):

        print(f'自定义中间件，响应: {request.path}')

        return response