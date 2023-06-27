from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request): # http相关请求信息 -- 封装成了 HttpRequest对象

    if request.method == 'GET':
        print(request.GET)
        print(request.META)  # 请求头相关信息
        return render(request, 'index.html')
    else:
        print(request.method)
        print(request.body) # 请求提交数据的原始数据,byte数据类型: 例如 b'username=erwei.zheng'
        print(request.path)
        print(request.path_info)
        print(request.get_full_path())

        print(request.META) # 请求头相关信息

        print(request.POST)

        return HttpResponse('post请求')

def login(request):

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'taibai' and password == 'dsb':
            # return render(request, 'home.html')
            return redirect('/home/')
        else:
            return HttpResponse('滚犊子，赶紧去充钱')

# 首页
def home(request):
    return render(request, 'home.html')