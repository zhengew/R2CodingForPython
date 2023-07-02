from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    num = 100
    name = '大壮'
    name_list = ['大壮', '雪飞', 'B哥']
    d1 = {'name': '大壮', 'age': 73, 'hobby': 'xuefei+xiangxi'}

    class Animal(object):
        def __init__(self):
            self.kind = 'dog'
        def eat(self):
            return 'shi'
    xiaobai = Animal()
    xx = 'OO'

    moviesize = 1234567891

    import datetime
    now = datetime.datetime.now()

    words = 'i love you '

    tag = '<a href="https://www.baidu.com" target="_blank">百度</a>'

    # return render(request, 'index.html', {'num': num, 'name': name, 'name_list': name_list,
    #             'd1': d1, 'xiaobai': xiaobai, 'xx': xx, 'moviesize': moviesize})
    return render(request, 'index.html', locals()) # 简写，不建议使用， locals(): 当前执行脚本中的所有全局变量

def tags(request):
    num = 10
    name_list = ['大壮', '雪飞', 'B哥']
    d1 = {'name': '大壮', 'age': 73, 'hobby': ['雪飞', 'B哥', 'ALEX']}
    d3 = []
    return render(request, 'tags.html', locals())

def csrf_token_login(request):
    if request.method == 'GET':
        return render(request, 'csrf_token_login.html')
    elif request.method == 'POST':
        print(request.POST)
        return HttpResponse('%s,登录成功～' % request.POST.get('username'))