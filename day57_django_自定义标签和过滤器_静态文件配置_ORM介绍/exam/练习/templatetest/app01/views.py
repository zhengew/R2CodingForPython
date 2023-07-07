from django.shortcuts import render, HttpResponse

# Create your views here.


def app01Index(request):
    return HttpResponse('基础估值配置')


# 验证自定义过滤器
def app01myfilter(request):

    content = 'hello world myfilter'
    name = 'xuefei'
    sex = 'female'
    age = 18
    return render(request, 'myfilter.html', {'content': content, 'name': name, 'sex': sex, 'age': age})


# 验证自定义标签
def app01mytags(request):
    name = 'dazhuang'
    sex = 'male'
    age = 20
    return render(request, 'mytags.html', {'name': name, 'sex': sex, 'age': age})