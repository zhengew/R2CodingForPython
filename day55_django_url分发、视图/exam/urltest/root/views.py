from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def home(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.META['HTTP_USER_AGENT'])
        print(request.path)
        print(request.path_info)
        print(request.get_full_path())
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(request.POST) # post请求数据
        print(request.body) # post请求提交的数据，byte类型

        if username == 'zew' and password == '123':
            # return render(request, 'home.html')
            return redirect('/home/')
        else:
            return HttpResponse('用户名或密码错误')
# 重定向到首页
def index(request):
    return render(request, 'home.html')