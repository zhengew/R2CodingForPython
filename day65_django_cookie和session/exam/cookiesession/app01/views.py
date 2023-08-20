from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# 登录认证 装饰器
def loginauth(f):

    def inner(request, *args, **kwargs):
        is_login = request.COOKIES.get('is_login')
        if is_login == 'True':
            ret = f(request, *args, **kwargs)
            return ret
        else:
            return redirect('login')

    return inner
#
def root(request):
    if request.path == '/':
        return redirect('login')
# def login(request, *args, **kwargs):
#
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         if username == 'zew' and password == '123':
#             ret = redirect('home')
#             ret.set_cookie('is_login', True, max_age=10) # max_age 设置cookie失效时间，单位秒
#
#             # 删除 cookie
#             # ret.delete_cookie('is_login') # 推出时使用
#
#             return ret
#         else:
#             return redirect('login')

# def index(request, *args, **kwargs):
#
#     ret = HttpResponse('200 ok')
#     ret.set_cookie('k1', 'v1')
#     return ret

# def index(request, *args, **kwargs):
#
#     is_login = request.COOKIES.get('is_login')
#     print(is_login, type(is_login))
#
#     if is_login == 'True':
#         return render(request, 'index.html')
#     else:
#         return redirect('login')

# @loginauth
# def index(request, *args, **kwargs):
#
#     return render(request, 'index.html')


# def home(request, *args, **kwargs):
#
#     print(request.COOKIES)
#     is_login = request.COOKIES.get('is_login')
#
#     if is_login == 'True':
#         return render(request, 'home.html')
#     else:
#         return redirect('login')

# @loginauth
# def home(request):
#     return render(request, 'home.html')



 # session 示例

def home(request, *args, **kwargs):

    print(request.session)
    # is_login = request.session['is_login'] # 直接取如果 session 被清空会报错，使用 get 来获取字典key的value
    is_login = request.session.get('is_login')
    '''
      1. 从 cookie 里面拿出了 sessionid 这个随机字符串
      2. 去 django_session 表里查询到对应的数据
      3. 反解加密的用户数据，并获取用户需要的数据
    '''

    print(is_login, type(is_login))  # True
    if is_login == True:
        return render(request, 'home.html')
    else:
        return redirect('login')


def login(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'zew' and password == '123':
            # ret = redirect('home') # cookie通过响应对象设置
            # cookie 可以设置多个键值对
            # ret.set_cookie('is_login', True)
            # ret.set_cookie('sex', 'male')
            # ret.set_cookie('username', 'zew')
            # return ret

            '''
            两种引入配置文件区别：
            # from django.conf import settings  先在用户配置文件找，找不到再去 global_settins文件中找
            # from  django.conf import global_settings 直接在global_settings 中找， 不会去看用户的settings配置文件
            # 推荐使用 第一种方式

            '''
            # session 示例
            request.session['is_login'] = True
            request.session['username'] = 'zew'
            # 1. 生成了 sessionid: 随机字符串
            # 2. 在 cookie 里面加上了一个键值对: sessionid: xxx
            # 3. 将用户的数据进行了加密，并保存到 django_session 表里
            '''
             session_key    session_data            expire_date
              随机字符串        用户数据加密后的字符串     过期时间
            '''

            return redirect('home')
        else:
            return redirect('login')

def logout(request):

    request.session.flush() # 清空 django_session表的session 和 浏览器cookie
    return redirect('login')