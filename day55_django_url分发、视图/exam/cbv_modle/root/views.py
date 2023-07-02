from django.shortcuts import render, HttpResponse
from django.views import View # CBV 模式的父类 View
from django.utils.decorators import method_decorator # cbv 加装饰器
import time
# 装饰器函数
def wrapper(f):
    def inner(*args, **kwargs):
        start = time.time()
        print('请求之前:%s' %start)
        ret = f(*args, **kwargs)
        stop = time.time()
        print('请求结束:%s, 请求耗时:%s' % (stop, stop - start))
        return ret
    return inner

# CBV 视图编写模式
@method_decorator(wrapper, name='get') # 方式三 给视图类加装饰器，name参数可指定视图类中的方法
class LoginView(View):

    @method_decorator(wrapper) # 方式二 给所有的方法加装饰器
    # dispath 反射自动识别不同的请求路径
    def dispatch(self, request, *args, **kwargs):
        print('root请求来了:%s' % request.path)
        ret = super().dispatch(request, *args, **kwargs)
        print('root请求结束:%s' % request.path)
        return ret
    def get(self, request):
        print('root中的get方法执行了')
        return render(request, 'login.html')

    @method_decorator(wrapper) # 方式一 给指定方法加装饰器
    def post(self, request):
        print('root中的post方法执行了')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if username == 'zew' and password == '123':
            return render(request, 'home.html')
        else:
            return HttpResponse('用户名或密码错误')

