from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

class App01View(View):

    def dispatch(self, request, *args, **kwargs):
        print('app01的请求:%s' % request.path)
        ret = super().dispatch(request, *args, **kwargs)
        print('app01请求结束:%s' % request.path)
        return ret

    def get(self, request):
        print('app01中的get方法执行了')
        return HttpResponse('app01应用首页')