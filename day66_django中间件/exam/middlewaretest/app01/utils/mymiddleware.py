# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: mymiddleware.py
# @datatime: 2023/9/7 23:32

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import (
    redirect, HttpResponse, render
)


from utils.logUtils.logControl import DEBUG

class SessionAuth(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):
        DEBUG.logger.debug(f'自定中间件请求来了')
        white_url = [reverse('login')]

        if request.path in white_url:
            return None

        is_login = request.session.get('is_login', None)
        if is_login:
            return None
        else:
            return redirect('login')






    def process_response(self, request, response, *args, **kwargs):

        DEBUG.logger.debug(f'自定义中间件响应来了')
        return response
