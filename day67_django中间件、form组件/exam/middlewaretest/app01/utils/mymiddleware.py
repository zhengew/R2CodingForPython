# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: mymiddleware.py
# @datatime: 2023/9/7 23:32

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import (
    redirect, HttpResponse, render
)
from django.conf import settings

from utils.logUtils.logControl import DEBUG,INFO

# 演示中间件 session 认证
class SessionAuth(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):
        DEBUG.logger.debug(f'自定义中间件请求来了')
        # 白名单
        if request.path in settings.WHITE_URL:
            return None

        is_login = request.session.get('is_login', None)
        if is_login:
            return None
        else:
            return redirect('login')

    def process_response(self, request, response, *args, **kwargs):

        DEBUG.logger.debug(f'自定义中间件响应来了')
        return response


#  演示 process_view
class MD1(MiddlewareMixin):

    def process_request(self, request):
        DEBUG.logger.debug(f'MD1 process_request')
        # IP地址访问限制
        INFO.logger.info(f'客户端IP地址:{request.META.get("REMOTE_ADDR")}')

    def process_view(self, request, view_func, view_args, view_kwargs):

        DEBUG.logger.debug(f'MD1 process_view: {view_func.__name__}')


    def process_response(self, request, response):

        DEBUG.logger.debug(f'MD1 process_response:{response}')
        return response

    def process_exception(self, request, response):
        DEBUG.logger.debug(f'md1 错误')

class MD2(MiddlewareMixin):

    def process_request(self, request):
        DEBUG.logger.debug(f'MD2 process_request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        DEBUG.logger.debug(f'MD2 process_view: {view_func.__name__}')

    def process_response(self, request, response):
        DEBUG.logger.debug(f'MD2 process_response:{response}')
        return response

    def process_exception(self, request, response):

        DEBUG.logger.debug(f'md2 错误')