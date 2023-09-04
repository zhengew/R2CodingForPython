# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: mymiddleware.py
# @datatime: 2023/9/4 20:56

from django.utils.deprecation import MiddlewareMixin

class MD1(MiddlewareMixin):

    def process_request(self, request):

        print('MD1请求来了')
        return None

    def process_response(self, request, response):

        print('MD1响应来了')
        return response


class MD2(MiddlewareMixin):

    def process_request(self, request):

        print('MD2请求来了')
        return None

    def process_response(self, request, response):

        print('MD2响应来了')
        return response