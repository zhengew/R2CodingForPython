# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: mymiddleware.py
# @datatime: 2023/9/7 23:32

from django.utils.deprecation import MiddlewareMixin

from utils.logUtils.logControl import DEBUG

class MyMiddleWare(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):

        DEBUG.logger.debug(f'自定中间件请求来了')
        return None

    def process_response(self, request, response, *args, **kwargs):

        DEBUG.logger.debug(f'自定义中间件响应来了')
        return response
